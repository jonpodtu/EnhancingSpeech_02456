# load packages
import random
import yaml
from munch import Munch
import numpy as np
import torch
from torch import nn
import torch.nn.functional as F
import torchaudio
import librosa
from parallel_wavegan.utils import load_model
import os
import time
import soundfile as sf

# import sys
# sys.path.append("src/stargan")

from stargan.Utils.ASR.models import ASRCNN
from stargan.Utils.JDC.model import JDCNet
#from stargan.models_depthwise_convolutions import Generator, MappingNetwork, StyleEncoder

DEPTHWISE_CONVOLUTION = True

if DEPTHWISE_CONVOLUTION:
    from stargan.models_depthwise_convolutions import Generator, MappingNetwork, StyleEncoder
else:
    from stargan.models import Generator, MappingNetwork, StyleEncoder



# Source: http://speech.ee.ntu.edu.tw/~jjery2243542/resource/model/is18/en_speaker_used.txt
# Source: https://github.com/jjery2243542/voice_conversion

speakers = [
    "225",
    "228",
    "229",
    "230",
    "231",
    "233",
    "236",
    "239",
    "240",
    "244",
    "226",
    "227",
    "232",
    "243",
    "254",
    "256",
    "258",
    "259",
    "270",
    "273",
    "225_filter",
    "228_filter",
    "229_filter",
    "230_filter",
    "231_filter",
    "233_filter",
    "236_filter",
    "239_filter",
    "240_filter",
    "244_filter",
    "226_filter",
    "227_filter",
    "232_filter",
    "243_filter",
    "254_filter",
    "256_filter",
    "258_filter",
    "259_filter",
    "270_filter",
    "273_filter",
]

speakers = ["001", "001_filter"]

to_mel = torchaudio.transforms.MelSpectrogram(
    n_mels=80, n_fft=2048, win_length=1200, hop_length=300
)
mean, std = -4, 4


def preprocess(wave):
    wave_tensor = torch.from_numpy(wave).float()
    mel_tensor = to_mel(wave_tensor)
    mel_tensor = (torch.log(1e-5 + mel_tensor.unsqueeze(0)) - mean) / std
    return mel_tensor


def build_model(model_params={}):
    args = Munch(model_params)
    generator = Generator(
        args.dim_in,
        args.style_dim,
        args.max_conv_dim,
        w_hpf=args.w_hpf,
        F0_channel=args.F0_channel,
    )
    mapping_network = MappingNetwork(
        args.latent_dim, args.style_dim, args.num_domains, hidden_dim=args.max_conv_dim
    )
    style_encoder = StyleEncoder(
        args.dim_in, args.style_dim, args.num_domains, args.max_conv_dim
    )

    nets_ema = Munch(
        generator=generator,
        mapping_network=mapping_network,
        style_encoder=style_encoder,
    )

    return nets_ema


def compute_style(speaker_dicts, starganv2):
    reference_embeddings = {}
    for key, (path, speaker) in speaker_dicts.items():
        if path == "":
            label = torch.LongTensor([speaker]).to("cuda")
            latent_dim = starganv2.mapping_network.shared[0].in_features
            ref = starganv2.mapping_network(
                torch.randn(1, latent_dim).to("cuda"), label
            )
        else:
            wave, sr = librosa.load(path, sr=24000)
            audio, index = librosa.effects.trim(wave, top_db=30)
            if sr != 24000:
                wave = librosa.resample(wave, sr, 24000)
            mel_tensor = preprocess(wave).to("cuda")

            with torch.no_grad():
                label = torch.LongTensor([speaker])
                ref = starganv2.style_encoder(mel_tensor.unsqueeze(1), label)
        reference_embeddings[key] = (ref, label)

    return reference_embeddings

    # load F0 model


if __name__ == "__main__":
    save_folder = "Data/Test_DTU"

    F0_model = JDCNet(num_class=1, seq_len=192)
    params = torch.load("src/stargan/Utils/JDC/bst.t7")["net"]
    F0_model.load_state_dict(params)
    _ = F0_model.eval()
    F0_model = F0_model.to("cuda")

    # load vocoder
    vocoder = (
        load_model("src/stargan/Vocoder/checkpoint-400000steps.pkl").to("cuda").eval()
    )
    vocoder.remove_weight_norm()
    _ = vocoder.eval()

    # load starganv2

    model_path = "outputs/BeamMeUpScottieA100/epoch_00100.pth"

    with open("outputs/BeamMeUpScottieA100/config.yml") as f:
        starganv2_config = yaml.safe_load(f)
    starganv2 = build_model(model_params=starganv2_config["model_params"])
    params = torch.load(model_path, map_location="cpu")
    params = params["model_ema"]
    _ = [starganv2[key].load_state_dict(params[key]) for key in starganv2]
    _ = [starganv2[key].eval() for key in starganv2]
    starganv2.style_encoder = starganv2.style_encoder.to("cuda")
    starganv2.mapping_network = starganv2.mapping_network.to("cuda")
    starganv2.generator = starganv2.generator.to("cuda")

    # load input wave
    wav_path = "Data/DTU/p001_filter/DTU.wav"  # "Data/VCTK/Data/p228_filter/1.wav"
    audio, source_sr = librosa.load(wav_path, sr=24000)
    audio = audio / np.max(np.abs(audio))
    audio.dtype = np.float32
    source = preprocess(audio).to("cuda:0")

    # MAKE SPEAKER DICT FOR FINAL CONVERSION type reference
    speaker_dicts = {}
    selected_speakers = [
        "001",
        "001_filter",
    ]
    for s in selected_speakers:
        k = s
        speaker_dicts["p" + str(s)] = (
            "Data/DTU" + "/p" + str(k) + "/DTU_style.wav",
            speakers.index(s),
        )
        # speaker_dicts["p" + str(s)] = (
        #    "Data/VCTK/Data" + "/p" + str(k) + "/2.wav",
        #    speakers.index(s),
        # )

    reference_embeddings = compute_style(speaker_dicts, starganv2)

    keys = []
    converted_samples = {}
    reconstructed_samples = {}
    converted_mels = {}

    for key, (ref, _) in reference_embeddings.items():
        with torch.no_grad():
            f0_feat = F0_model.get_feature_GAN(source.unsqueeze(1))
            out = starganv2.generator(source.unsqueeze(1), ref, F0=f0_feat)

            c = out.transpose(-1, -2).squeeze().to("cuda")
            y_out = vocoder.inference(c)
            y_out = y_out.view(-1).cpu()

            if key not in speaker_dicts or speaker_dicts[key][0] == "":
                recon = None
            else:
                wave, sr = librosa.load(speaker_dicts[key][0], sr=24000)
                mel = preprocess(wave)
                c = mel.transpose(-1, -2).squeeze().to("cuda")
                recon = vocoder.inference(c)
                recon = recon.view(-1).cpu().numpy()

        converted_samples[key] = y_out.numpy()
        reconstructed_samples[key] = recon

        if not os.path.exists(save_folder):
            os.mkdir(save_folder)
            # Write out audio
        sf.write(
            os.path.join(save_folder, "{}.wav".format(key)),
            y_out.numpy(),
            samplerate=24000,
        )

        converted_mels[key] = out

        keys.append(key)

print("All Done")

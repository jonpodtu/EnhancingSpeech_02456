import sys
sys.path.append("../src")
import soundfile as sf
import torch 
from stargan.Utils.mel_spectrograms import *

wave_path = "stargan/Data/p225/1.wav"

wave, sr = sf.read(wave_path)
wave_tensor = torch.from_numpy(wave).float()

mel_tensor = wav2mel(wave_tensor)

melplot(mel_tensor, save = True)

print(mel_tensor)

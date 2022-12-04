import torchaudio
import numpy as np
import torch
import matplotlib.pyplot as plt
import librosa

def wav2mel(wav, max_mel_length = 192, n_mels=80, n_fft=2048, win_length=1200, hop_length=300):
    '''
    Input is a wavefile, given as a tensor, output is a mel tensor
    '''
    mean = -4
    std = 4
    to_melspec = torchaudio.transforms.MelSpectrogram(n_mels = n_mels, n_fft = n_fft, win_length = win_length, hop_length = hop_length)
    mel_tensor = to_melspec(wav)
    #mel_tensor = torch.log(mel_tensor)
    # If normalize:
    mel_tensor = (torch.log(1e-5 + mel_tensor) - mean) / std
    mel_length = mel_tensor.size(1)
    if mel_length > max_mel_length:
            random_start = np.random.randint(0, mel_length - max_mel_length)
            mel_tensor = mel_tensor[:, random_start:random_start + max_mel_length]
    return mel_tensor

def melplot(spec, title=None, ylabel='freq_bin', aspect='auto', xmax=None, save = False):
    fig, axs = plt.subplots(1, 1)
    axs.set_title(title or 'Spectrogram')
    axs.set_ylabel(ylabel)
    axs.set_xlabel('frame')
    im = axs.imshow(spec, origin='lower', aspect=aspect)
    if xmax:
        axs.set_xlim((0, xmax))
    fig.colorbar(im, ax=axs)
    if save:
        plt.savefig('mel_spectrogram'+'.png', bbox_inches = 'tight')
    plt.show(block=False)




from scipy.signal import lfilter, butter
from scipy.io.wavfile import read,write
from numpy import array, int16
import soundfile as sf
import sys
import os
from math import floor
import random
from tqdm import tqdm
import argparse

def butter_params(low_freq, high_freq, fs, order=5):
    nyq = 0.5 * fs
    low = low_freq / nyq
    high = high_freq / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, low_freq, high_freq, fs, order=5):
    b, a = butter_params(low_freq, high_freq, fs, order=order)
    y = lfilter(b, a, data)
    return y

if __name__ == '__main__':
    inargs = argparse.ArgumentParser()
    inargs.add_argument(
        "--liststyles",
        nargs="*",
        type=str,
        default=['p228', 'p225', 'p233'],
    )

    data_path = 'Data'
    args = inargs.parse_args()

    for speaker in tqdm(args.liststyles):
        # List files:
        files = os.scandir("Data/"+speaker)
        for file in files:
            filepath = "Data/"+speaker+"/"+file.name
            fs, audio = read("Data/"+speaker+"/"+file.name)
            low_freq = 300.0
            high_freq = 3400.0
            filtered_signal = butter_bandpass_filter(audio, low_freq, high_freq, fs, order=6)
            fname = filepath
            write(fname,fs,array(filtered_signal,dtype=int16))
from scipy.signal import lfilter, butter
from scipy.io.wavfile import read, write
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
    b, a = butter(order, [low, high], btype="band")
    return b, a


def butter_bandpass_filter(data, low_freq, high_freq, fs, order=5):
    b, a = butter_params(low_freq, high_freq, fs, order=order)
    y = lfilter(b, a, data)
    return y


if __name__ == "__main__":
    inargs = argparse.ArgumentParser()
    inargs.add_argument(
        "--liststyles",
        nargs="*",
        type=str,
        default=["p228", "p225", "p233"],
    )

    args = inargs.parse_args()
    speakers = args.liststyles

    vctk_dir = "Data"
    os.chdir(vctk_dir)

    data_path = "DTU"
    out_data_path = "DTU"

    speakers = []
    random.seed(42)
    for entry in os.listdir(data_path):
        if os.path.isdir(os.path.join(data_path, entry)):
            if entry[0] == "p":
                speakers.append(entry)
    #     Choose random speakers:
    # no_sample = floor(len(speakers) / 2)
    # chosen_speakers = random.sample(speakers, no_sample)
    chosen_speakers = speakers

    print(speakers)

    for speaker in tqdm(speakers):
        # List files:
        output_dir = os.path.join(out_data_path, speaker + "_filter")
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        scan_directory = os.path.join(data_path, speaker)
        files = os.scandir(scan_directory)
        for file in files:
            filepath = os.path.join(scan_directory, file.name)
            fs, audio = read(filepath)
            low_freq = 300.0
            high_freq = 3400.0
            filtered_signal = butter_bandpass_filter(
                audio, low_freq, high_freq, fs, order=6
            )
            out_fname = os.path.join(output_dir, file.name)
            write(out_fname, fs, array(filtered_signal, dtype=int16))

# Speakers transformed:
# ['p254', 'p270', 'p273', 'p230', 'p259', 'p240', 'p244', 'p225', 'p227', 'p233']

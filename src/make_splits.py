# output path
__OUTPATH__ = "./Data/VCTK/Data"

import pandas as pd
import random
import os

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
data_list = []
for path, subdirs, files in os.walk(__OUTPATH__):
    for name in files:
        if name.endswith(".wav"):
            speaker = path.split("/")[-1].replace("p", "")
            if speaker in speakers:
                data_list.append(
                    {
                        "Path": os.path.join(path, name),
                        "Speaker": int(speakers.index(speaker)) + 1,
                    }
                )


data_list = pd.DataFrame(data_list)
data_list = data_list.sample(frac=1)

# We simply make a hold out validation
split_idx = round(len(data_list) * 0.1)
test_data = data_list[:split_idx]
train_data = data_list[split_idx:]

# write to file
file_str = ""
for index, k in train_data.iterrows():
    file_str += k["Path"] + "|" + str(k["Speaker"] - 1) + "\n"
text_file = open(__OUTPATH__ + "/train_list.txt", "w")
text_file.write(file_str)
text_file.close()

file_str = ""
for index, k in test_data.iterrows():
    file_str += k["Path"] + "|" + str(k["Speaker"] - 1) + "\n"
text_file = open(__OUTPATH__ + "/val_list.txt", "w")
text_file.write(file_str)
text_file.close()

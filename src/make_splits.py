# output path
__OUTPATH__ = "./Data/VCTK/Data"

import pandas as pd
import random
import os
from sklearn.model_selection import train_test_split

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
]

def phone_or_not():
    return random.choice(["", "_filter"])

data_list = []
for path, subdirs, files in os.walk(__OUTPATH__):
    for name in files:

        if name.endswith(".wav"):
            speaker = path.split("/")[-1].replace("p", "")
            if speaker in speakers:
                toss = phone_or_not() # Simple coin toss to get half non-filter - half filtered
                if toss ==  "_filter":
                    add_index = 21
                else:
                    add_index = 1
                data_list.append(
                    {
                        "Path": os.path.join(path + toss, name),
                        "Speaker": int(speakers.index(speaker)) + add_index,
                    }
                )


data_list = pd.DataFrame(data_list)
print(data_list)

train_data, test_data = train_test_split(data_list, test_size=0.1, random_state=0, stratify=data_list[['Speaker']])

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

import shutil
import os

def get_data_path_list():
    with open("Data/VCTK/Data/val_list.txt", 'r') as f:
        val_list = f.readlines()
    return val_list

data_list = get_data_path_list()
_data_list = [l[:-1].split('|') for l in data_list]

# Lets sort out the test files 
data_paths = [path for path, label in _data_list if int(label) > 19]

# And their targets
data_org = [path.replace("_filter", "") for path in data_paths]

# References
data_refs = [path for path, label in _data_list if int(label) < 20]

#os.makedirs("Data/valid/val")
#os.makedirs("Data/valid/target")
#os.makedirs("Data/valid/refs")

val_path = 'Data/valid/val'
for p in data_paths:
    filename = p.split('/')[-2:]
    cur_dir = os.path.join(val_path, filename[0])
    if not os.path.exists(cur_dir):
        os.makedirs(cur_dir)
    shutil.copyfile(p, os.path.join(val_path, '/'.join(filename)))

target_path = 'Data/valid/target'
for p in data_org:
    filename = p.split('/')[-2:]
    cur_dir = os.path.join(target_path, filename[0])
    if not os.path.exists(cur_dir):
        os.makedirs(cur_dir)
    shutil.copyfile(p, os.path.join(target_path, '/'.join(filename)))

refs_path='Data/valid/refs'
for p in data_refs:
    filename = p.split('/')[-2:]
    cur_dir = os.path.join(refs_path, filename[0])
    if not os.path.exists(cur_dir):
        os.makedirs(cur_dir)
    shutil.copyfile(p, os.path.join(refs_path, '/'.join(filename)))
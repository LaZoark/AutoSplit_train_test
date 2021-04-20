import os
import numpy as np
import shutil
from alive_progress import alive_bar
from sys import exit
import glob
from os.path import join
# import warnings
# warnings.simplefilter('error', UserWarning)
# file_type = '.xml'
if __name__ == '__main__':
    from sys import argv
    if len(argv) != 5:
        exit('[ERROR] requiring <root_dir> <data_folder_name> <train_folder_name> <test_folder_name>')
    root_dir = argv[1]  # data root path. Dir that contain all class of folder
    src = join(root_dir, argv[2])
    train_path = join(root_dir, argv[3])
    test_path = join(root_dir, argv[4])

print("Your config, please check:")
print("root_path  = %s" %root_dir)
print("data_path  = %s" %src)
print("train_path = %s" %train_path)
print("test_path  = %s" %test_path)
correct = input('Is it correct ?[Y/n]')
if correct == 'n' or correct == 'N':
    exit()

test_ratio = 0.30

if not os.path.exists(train_path):
    os.makedirs(train_path)
if not os.path.exists(test_path):
    os.makedirs(test_path)
# %%
allFileNames = glob.glob(join(src, '*.jpg'))
np.random.shuffle(allFileNames)
names = [os.path.splitext(_name) for _name in allFileNames]
names = [_name[0] for _name in names]
names = [os.path.basename(_name) for _name in names]

# %%
train_FileNames, test_FileNames = np.split(np.array(names),[int(len(names)* (1 - test_ratio))])

train_FileNames = [name for name in train_FileNames.tolist()]
test_FileNames = [name for name in test_FileNames.tolist()]

print("*****************************")
print('Total images : ', len(allFileNames))
print('Training     : ', len(train_FileNames))
print('Testing      : ', len(test_FileNames))
print("*****************************")
# %%
check_file = len(os.listdir(train_path))
if check_file > 0:
    # warnings.warn('There are %d files in "%s". \nMaybe something went wrong...?' %(check_file, train_path))
    confirm = input('[Warning!] There are %d files in "%s". \nMaybe something went wrong, proceed or not?[y/N]' %(check_file, train_path))
    if confirm == 'y' or confirm == 'Y':
        pass
    else:
        exit()
items = range(len(train_FileNames))
with alive_bar(len(items),"Splitting to 'train' folder") as bar:
    for name in train_FileNames:
        shutil.copyfile(join(src, name +'.jpg'), join(train_path, name +'.jpg'))
        shutil.copyfile(join(src, name +'.xml'), join(train_path, name +'.xml'))
        bar()
check_file = len(os.listdir(test_path))
if check_file > 0:
    confirm = input('[Warning!] There are %d files in "%s". \nMaybe something went wrong, proceed or not?[y/N]' %(check_file, test_path))
    if confirm == 'y' or confirm == 'Y':
        pass
    else:
        exit()
items = range(len(test_FileNames))
with alive_bar(len(items),"Splitting to 'test' folder") as bar:
    for name in test_FileNames:
        shutil.copyfile(join(src, name +'.jpg'), join(test_path, name +'.jpg'))
        shutil.copyfile(join(src, name +'.xml'), join(test_path, name +'.xml'))
        bar()
        
print("Copying Done!")


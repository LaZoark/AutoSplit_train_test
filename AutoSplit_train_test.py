import os
import numpy as np
import shutil
from alive_progress import alive_bar
from sys import exit
import glob
# import warnings
# warnings.simplefilter('error', UserWarning)

# file_type = '.xml'
root_dir = "D:\\NewSample" # data root path
src = os.path.join(root_dir,'data')
train_path = os.path.join(root_dir,'Train')
test_path = os.path.join(root_dir,'Test')
test_ratio = 0.30

if not os.path.exists(train_path):
    os.makedirs(train_path)
if not os.path.exists(test_path):
    os.makedirs(test_path)
# %%
# allFileNames = os.listdir(src)
allFileNames = glob.glob(src + '\\*.jpg')
np.random.shuffle(allFileNames)
# for _name in allFileNames:
#     names.append(os.path.splitext(_name))
names = [os.path.splitext(_name) for _name in allFileNames]
names = [_name[0] for _name in names]
names = [os.path.basename(_name) for _name in names]
# temp = glob.glob('D:\\NewSample\\bottle\\' + 'P_20210321_111419.*')

# %%
train_FileNames, test_FileNames = np.split(np.array(names),[int(len(names)* (1 - test_ratio))])

train_FileNames = [name for name in train_FileNames.tolist()]
test_FileNames = [name for name in test_FileNames.tolist()]

print("*****************************")
print('Total images: ', len(allFileNames))
print('Training: ', len(train_FileNames))
print('Testing: ', len(test_FileNames))
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
        shutil.copyfile(src +"\\"+ name +'.jpg', train_path +"\\"+ name +'.jpg')
        shutil.copyfile(src +"\\"+ name +'.xml', train_path +"\\"+ name +'.xml')
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
        shutil.copyfile(src +"\\"+ name +'.jpg', test_path +"\\"+ name +'.jpg')
        shutil.copyfile(src +"\\"+ name +'.xml', test_path +"\\"+ name +'.xml')
        bar()
        
print("Copying Done!")
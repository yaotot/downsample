import os
import pandas as pd


def get_file_list(folder):
    file_list = []
    for root,dirs,files  in os.walk(folder):
        for file in files:
            if file.endswith('BLG.csv'):
                file_list.append(os.path.join(root,file))

    return file_list


root_folder='R:\data'
# for root,dirs,files in os.walk(root_folder):
#     print('root',root)
#     print('dirs',dirs)
#     print('files',files)
#     print("++++++++++++++++++++++++++++++")
file_list = get_file_list(root_folder)
print(file_list)


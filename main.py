import numpy as np
import os
import pandas as pd
from scipy.interpolate import CubicSpline,interp1d


def process_file(input_file_path, output_directory,target_hz,orgin_hz=1000):
    data = pd.read_csv(input_file_path)
    data.drop(['dP', 'lab', 'xT', 'yT'], axis=1, inplace=True)
    # while data.iloc[-1]['val']==4:
    #     data.drop(data.index[-1],inplace=True)
    #
    # while data.iloc[0]['val']==4:
    #     data.drop(data.index[0],inplace=True)

    data.drop(data[data['val']==4].index, inplace=True)
    data.drop(['val', 'n'], axis=1, inplace=True)
    data=data.round(6)
    step = int(orgin_hz/target_hz)
    num_groups = step

    for i in range(num_groups):
        start_index = i
        downsampled_data = data.iloc[start_index :: step]
        filename = os.path.splitext(os.path.basename(input_file_path))[0]
        output_file= os.path.join(output_directory,f"downsampled_{filename}_{i+1}.csv")
        downsampled_data.to_csv(output_file, index=0)
        print(f'Processed file:{input_file_path}')

    #invalid_point = data['val'] == 4
    #interp_func = CubicSpline(data.loc[~invalid_point].index, data.loc[~invalid_point,['x','y']])   #cubic
    #interp_func = interp1d(data.loc[~invalid_point].index, data.loc[~invalid_point,['x','y']],kind='linear', axis=0)   #linear
    #data.loc[invalid_point,['x','y']] = interp_func(data.loc[invalid_point].index)

def process_csv_files_in_directory(root_directory):
    output_directory = 'R:\data\gazedata_downsample'
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith(".csv"):
                input_file_path = os.path.join(root,file)
                process_file(input_file_path,output_directory,50)

# def downsample (input_data,target_sample_rate,):


root_directory = 'R:\data\GazeBase_v2_0'
process_csv_files_in_directory(root_directory)


# data = pd.read_csv('csv\S_1001_S1_BLG.csv')
# data.drop(['dP', 'lab', 'xT', 'yT'], axis=1, inplace=True)
# print(os.path.splitext(os.path.basename('csv\S_1001_S1_BLG.csv'))[0])
# invalid_point = data['val'] == 4
# interp_func = CubicSpline(data.loc[~invalid_point].index, data.loc[~invalid_point,['x','y']])
# data.loc[invalid_point,['x','y']] = interp_func(data.loc[invalid_point].index)
# data.drop(['val','n'], axis=1, inplace=True)
# #print(data)
# data_array= data.to_numpy()
# # print("22222")
# # print(data_array)
# # print("333333")
# windows_size = 10
# num_windows = len(data_array)// windows_size
# windowed_data= [data_array[i*windows_size :(i+1)*windows_size] for i in range(num_windows)]
# windowed_tensor= np.array(windowed_data)
# #print(windowed_tensor)
# data = pd.read_csv('csv\S_1001_S1_BLG.csv')
# print(data)
# print("wwwww")
# loaded = np.load('ncsv\S_1001_S1_BLG.npy')
# print(loaded.shape)
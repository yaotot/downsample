import numpy as np
import os
import pandas as pd
from scipy.interpolate import CubicSpline,interp1d


def process_file(input_file_path, output_file_path):
    data = pd.read_csv(input_file_path)
    data.drop(['dP', 'lab', 'xT', 'yT'], axis=1, inplace=True)
    # while data.iloc[-1]['val']==4:
    #     data.drop(data.index[-1],inplace=True)
    print(data.iloc[0])
    while data.iloc[0]['val']==4:
        data.drop(data.index[0],inplace=True)

    print("----")
    print(data.iloc[0])
    # invalid_point = data['val'] == 4
    # #interp_func = CubicSpline(data.loc[~invalid_point].index, data.loc[~invalid_point,['x','y']])
    # interp_func = interp1d(data.loc[~invalid_point].index, data.loc[~invalid_point,['x','y']],kind='linear', axis=0)
    # data.loc[invalid_point,['x','y']] = interp_func(data.loc[invalid_point].index)
    # data.drop(['val','n'], axis=1, inplace=True)
    # data.to_csv(output_file_path,index=0)
    #

    print(f'Processed file:{input_file_path}')

process_file('R:\data\GazeBase_v2_0\Round_1\Subject_1002\S2\S2_Fixations\S_1002_S2_FXS.csv','\GazeBase_v2_0\Round_1\Subject_1002\S2\S2_Fixations')
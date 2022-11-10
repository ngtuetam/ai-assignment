import cv2
import numpy as np
import csv
import pandas as pd
from calc_humomment import caculate_HuMM
from get_feature import get_features, get_feature
from write_data import write_file
from write_data import write_data_train


def split_data(file_path_base, feature_A, feature_B):
    A_features = pd.read_csv(f'{file_path_base}/features/{feature_A}_ft.csv').to_numpy()
    B_features = pd.read_csv(f'{file_path_base}/features/{feature_B}_ft.csv').to_numpy()
    test_data = np.zeros((10, 7))
    train_data_feature_A = np.zeros((40, 7))
    train_data_feature_B = np.zeros((40, 7))

    train_data_feature_A[0:8]   = A_features[2:10,:]
    train_data_feature_A[8:10]  = A_features[0:2,:]
    train_data_feature_A[10:16] = A_features[4:10,:]
    train_data_feature_A[16:20] = A_features[0:4,:]
    train_data_feature_A[20:24] = A_features[6:10,:]
    train_data_feature_A[24:30] = A_features[0:6,:]
    train_data_feature_A[30:32] = A_features[8:10,:]
    train_data_feature_A[32:40] = A_features[0:8,:]
    write_data_train(train_data_feature_A, A_features, feature_A)
    
    train_data_feature_B[0:8]   = B_features[2:10,:]
    train_data_feature_B[8:10]  = B_features[0:2,:]
    train_data_feature_B[10:16] = B_features[4:10,:]
    train_data_feature_B[16:20] = B_features[0:4,:]
    train_data_feature_B[20:24] = B_features[6:10,:]
    train_data_feature_B[24:30] = B_features[0:6,:]
    train_data_feature_B[30:32] = B_features[8:10,:]
    train_data_feature_B[32:40] = B_features[0:8,:]
    write_data_train(train_data_feature_B, B_features, feature_B)
    
    return train_data_feature_A, A_features, train_data_feature_B, B_features


if __name__ == "__main__":
    train_data_orange, test_data_orange, train_data_strawberry, test_data_strawberry = split_data('/home/ngtuetam/workspace/ai_assign/data_csv','orange','straw')
    
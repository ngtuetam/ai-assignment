import cv2
import numpy as np
from calc_humomment import caculate_HuMM
from write_data import write_file

def get_feature(str):
    feature_matrix = np.zeros((10,7))
    for i in range(0,10):
        tmp = caculate_HuMM(f'{str}{i}.jpg')
        for j in range(0,7):
            feature_matrix[i][j] = tmp[j]
    return feature_matrix

def get_features():
    lst = []
    orange_feature = get_feature('/home/ngtuetam/workspace/ai_assign/bin_imgs/orange_bin/image_')
    strawbery_feature = get_feature('/home/ngtuetam/workspace/ai_assign/bin_imgs/strawberry_bin/image_')
    # print(orange_feature)
    return orange_feature, strawbery_feature


# if __name__ == "__main__":
#     get_features()

if __name__ == "__main__":
    orange_feature, strawbery_feature = get_features()
    write_file(orange_feature,'/home/ngtuetam/workspace/ai_assign/data_csv/features/orange_ft')
    write_file(strawbery_feature,'/home/ngtuetam/workspace/ai_assign/data_csv/features/straw_ft')


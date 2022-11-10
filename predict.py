import math
import numpy as np
import pandas as pd


def predict(train_data_A, train_data_B, test_data, K_test=3):
    distance_array_B = np.zeros((8))
    distance_array_A = np.zeros((8))
    
    for row in range (8):
        for col in range (7):
            distance_array_B[row] += (train_data_A[row][col] - test_data[col])**2
        distance_array_B[row] = math.sqrt(distance_array_B[row])

    for row in range (8):
        for col in range (7):
            distance_array_A[row] += (train_data_B[row][col] - test_data[col])**2
        distance_array_A[row] = math.sqrt(distance_array_A[row])
        
    distance_array_A = np.sort(distance_array_A,kind='heapsort') 
    distance_array_B = np.sort(distance_array_B,kind='heapsort') 
    
    N_count = 0
    P_count = 0
    while (N_count + P_count) < K_test:
        if (distance_array_B[N_count] > distance_array_A[P_count]):
            P_count += 1
        else:
            N_count += 1
            
    if P_count > N_count:
        return "P"
    else:
        return "N"
    
if __name__ == "__main__":
    file_path = '/home/ngtuetam/workspace/ai_assign/data_csv/data_train'
    train_data_orange  = pd.read_csv(f'{file_path}/train_data_orange.csv').to_numpy()
    train_data_strawberry = pd.read_csv(f'{file_path}/train_data_strawberry.csv').to_numpy()
    test_data_orange   = pd.read_csv(f'{file_path}/test_data_orange.csv').to_numpy()
    test_data_strawberry  = pd.read_csv(f'{file_path}/test_data_strawberry.csv').to_numpy()

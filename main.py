import pandas as pd
from evaluation import test
from get_feature import get_feature, get_features
from write_data import write_file

if __name__ == "__main__":
    # get feature and write data feature
    
    # orange_feature, strawberry_feature = get_features()
    # write_file(orange_feature,'/home/ngtuetam/workspace/ai_assign/data_csv/fts/orange_features')
    # write_file(strawberry_feature,'/home/ngtuetam/workspace/ai_assign/data_csv/fts/straw_features')
    
    # PROCESS
    
    file_path = '/home/ngtuetam/workspace/ai_assign/data_csv/data_train'
    train_data_orange = pd.read_csv(
        f'{file_path}/train_data_orange.csv').to_numpy()
    train_data_straw = pd.read_csv(
        f'{file_path}/train_data_straw.csv').to_numpy()
    test_data_orange = pd.read_csv(
        f'{file_path}/test_data_orange.csv').to_numpy()
    test_data_straw = pd.read_csv(
        f'{file_path}/test_data_straw.csv').to_numpy()
    print("\nK = 3: ")
    RC, PR, ACC = test(train_data_orange, train_data_straw,
                       test_data_orange, test_data_straw, 3)
    print(f'RC: {RC}')
    print(f'PR: {PR}')
    print(f'ACC: {ACC}\n')
    print("K = 5: ")
    RC, PR, ACC = test(train_data_orange, train_data_straw,
                       test_data_orange, test_data_straw, 5)
    print(f'RC: {RC}')
    print(f'PR: {PR}')
    print(f'ACC: {ACC}')


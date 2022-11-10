import pandas as pd
from predict import predict

# sup lo P, ca chua N

def test(train_data_A, train_data_B, test_data_A, test_data_B, K_test=3):
    RC = 0.0
    PR = 0.0
    ACC = 0.0
    TP = 0.0
    FP = 0.0
    FN = 0.0
    TN = 0.0

    for i in range(0, 5):
        tmp = predict(
            train_data_B[i*8:i*8+8], train_data_A[i*8:i*8+8], test_data_A[i*2], K_test)
        if tmp == 'P':
            TP += 1
        else:
            FP += 1
        tmp = predict(
            train_data_B[i*8:i*8+8], train_data_A[i*8:i*8+8], test_data_A[i*2+1], K_test)
        if tmp == 'P':
            TP += 1
        else:
            FP += 1

        tmp = predict(
            train_data_B[i*8:i*8+8], train_data_A[i*8:i*8+8], test_data_B[i*2], K_test)
        if tmp == 'N':
            TN += 1
        else:
            FN += 1
        tmp = predict(
            train_data_B[i*8:i*8+8], train_data_A[i*8:i*8+8], test_data_B[i*2+1], K_test)
        if tmp == 'N':
            TN += 1
        else:
            FN += 1

    print(f'TP: {TP}')
    print(f'TN: {TN}')
    print(f'FN: {FN}')
    print(f'FP: {FP}')
    print('-----------')

    RC = round((TP / (TP + FN)),2)
    PR = round((TP / (TP + FP)),2)
    ACC = round(((TP + TN) / (TP + TN + FN + FP)),2)
    return RC, PR, ACC


if __name__ == "__main__":
    file_path = '/home/ngtuetam/workspace/ai_assign/data_csv/data_train'
    train_data_orange = pd.read_csv(
        f'{file_path}/train_data_orange.csv').to_numpy()
    train_data_straw = pd.read_csv(
        f'{file_path}/train_data_straw.csv').to_numpy()
    test_data_orange = pd.read_csv(
        f'{file_path}/test_data_orange.csv').to_numpy()
    test_data_straw = pd.read_csv(
        f'{file_path}/test_data_straw.csv').to_numpy()
    print("\nvoi k = 3: ")
    RC, PR, ACC = test(train_data_orange, train_data_straw,
                       test_data_orange, test_data_straw, 3)
    print(f'RC: {RC}')
    print(f'PR: {PR}')
    print(f'ACC: {ACC}\n')
    print("voi k = 5: ")
    RC, PR, ACC = test(train_data_orange, train_data_straw,
                       test_data_orange, test_data_straw, 5)
    print(f'RC: {RC}')
    print(f'PR: {PR}')
    print(f'ACC: {ACC}')

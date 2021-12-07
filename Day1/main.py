import pandas as pd

def read_input(file_name):
    with open(file_name) as f:
        data = [int(line.strip()) for line in f.readlines()]
        return data
 
def solve(data,windows):
    data_windowed = pd.Series(data).rolling(windows).sum().dropna().astype(int)
    return (data_windowed -  data_windowed.shift().fillna(0).astype(int)>= 1).sum() - 1 

if __name__ == "__main__":
    data = read_input('input.txt')
    print('solution part A:', solve(data,1))
    print('solution part B:', solve(data,3))
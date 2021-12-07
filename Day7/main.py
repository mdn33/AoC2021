import numpy as np

def read_input(file_name):
    with open(file_name) as f:
        data = [int(line.strip()) for line in f.readline().split(',')]
        return data
 
def solve(data):
    v = np.array([data])
    min_value = np.min(v)
    max_value = np.max(v)

    min_fuel = float('inf')
    for i in range(min_value,max_value+1):
        movements = np.abs(v-i)
        fuel = np.sum((movements*(movements+1)/2).astype(int))
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel
        
if __name__ == "__main__":
    data = read_input('input.txt')
    print('solution part B:', solve(data))
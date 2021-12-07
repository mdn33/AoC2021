import numpy as np
import math

class bingo_table ():
    def __init__(self,grid):
        self.grid = grid
        self.extractions = np.ones((grid.shape[0],grid.shape[1]))
    def check_number(self,number):
        for i in range(0,self.grid.shape[0]):
            for j in range(0,self.grid.shape[1]):
                if self.grid[i,j] == number:
                    self.extractions[i,j] = 0
    def check_solution(self):
        for i in range(0,self.extractions.shape[0]):
            if np.all(self.extractions[i,:]==0):
                return True
        for i in range(0,self.extractions.shape[1]):
            if np.all(self.extractions[:,i]==0):
                return  True
        return False
    def get_score(self):
        sum = 0 
        for i in range(0,self.grid.shape[0]):
            for j in range(0,self.grid.shape[1]):
                if self.extractions[i,j] == 1:
                    sum = sum + int(self.grid[i,j])
        return sum
    
def read_input_file(file_name = "input.txt",size = 25):
    bingo_tables = [] #list of bingo_table
    with open(file_name, "r") as fd:

        extracted_numbers = fd.readline().strip().split(',')
        numbers = []
        for line in fd:
            for number in line.replace('  ',' ').strip().split(' '):
                if number != '':
                    numbers.append(number)

    tables_number = len(numbers)/size
    numbers = np.array(numbers)

    for i in range(int(tables_number)):
        grid = numbers[i*size:i*size+size].reshape(int(np.sqrt(size)),int(np.sqrt(size)))
        bingo_tables.append(bingo_table(grid))
    return bingo_tables,extracted_numbers

def play_bingo ():
    winners = []
    grids,extracted_numbers = read_input_file()
    for extraction in extracted_numbers:
        for i,grid in enumerate(grids):
            grid.check_number(extraction)
            if grid.check_solution():
                if i not in winners:
                    winners.append(i)
                    unmarked_score = grid.get_score()
                    final_score = unmarked_score*int(extraction)
                    print(f' table {i+1} wins: {final_score}')
            
if __name__ == "__main__":         
    play_bingo()
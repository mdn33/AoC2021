import numpy as np
def read_input(file_name):
    grid = []
    with open(file_name) as f:
        for line in f:
            v = [int(digit) for digit in line.strip()]
            grid.append(v)
        return grid

def flash(grid,row,column):
    
    if grid[row,column] > 9 and [row,column] not in flashed:
        flashed.append([row,column])
        if row - 1 >= 0:
            grid[row-1,column] = 1 +  grid[row-1,column]
            if [row-1,column] not in flashed:
                grid = flash(grid, row - 1, column)
            if column -1 >= 0:
                grid[row-1,column-1] = 1 +  grid[row-1,column-1]
                if [row-1,column-1] not in flashed:
                    grid = flash(grid, row - 1, column-1)
            if column + 1 < grid.shape[1]: 
                grid[row-1,column+1] = 1 +  grid[row-1,column+1]
                if [row-1,column+ 1] not in flashed:
                    grid = flash(grid, row - 1, column+1) 
        if column - 1 >= 0:
            grid[row,column-1] = 1 +  grid[row,column-1]
            if [row,column-1] not in flashed:
                grid = flash(grid, row, column - 1)
        if row + 1 < grid.shape[0]:
            grid[row+1,column] = 1 +  grid[row+1,column]
            if [row+1,column] not in flashed:
                grid = flash(grid, row+1, column)
            if column -1 >= 0:
                grid[row + 1,column-1] = 1 +  grid[row+ 1,column-1]
                if [row + 1,column-1] not in flashed:
                    grid = flash(grid, row +  1, column-1)
            if column + 1 < grid.shape[1]:
                grid[row+1,column+1] = 1 +  grid[row+1,column+1]
                if [row+1,column+ 1] not in flashed:
                    grid = flash(grid, row + 1, column+1)
        if column + 1 < grid.shape[1]:  
            grid[row,column+1] = 1 +  grid[row,column+1]
            if [row,column+1] not in flashed :
                grid = flash(grid, row, column+1)
            
    return grid

def clean(grid):
    for row in range(grid.shape[0]):
        for column in range(grid.shape[1]):
            if grid[row,column] > 9:
                grid[row,column] = 0
    return grid

grid = np.array(read_input('iput.txt'))
step = 400
number_of_flashes = 0
all_flashed_step = -1
for i in range(step):
    flashed = []
    grid = grid + 1
    for row in range(grid.shape[0]):
        for column in range(grid.shape[1]):
            grid = flash(grid,row,column)
    grid = clean(grid)
    number_of_flashes += len(flashed)
    if len(flashed) == grid.shape[0]*grid.shape[1] and all_flashed_step == -1:
        all_flashed_step = 1 + i
        
print('answer part A:', number_of_flashes)
print('answer part B', all_flashed_step)
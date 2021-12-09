import numpy as np
def read_input(file_name):
    grid = []
    with open(file_name) as f:
        for line in f:
            v = [int(digit) for digit in line.strip()]
            grid.append(v)
        return grid
    
def explore(grid,i,j,k,visited = [],count=0):
    if grid[i,j] == 9:
        return grid
    else:
        grid[i,j] = k
        visited.append([i,j])
        count+=1
        if i-1 >= 0 and [i-1,j] not in visited:
            grid = explore(grid,i-1,j,k,visited,count)
        if i+1 < grid.shape[0] and [i+1,j] not in visited:
            grid = explore(grid,i+1,j,k,visited,count)
        if j - 1 >= 0 and [i,j-1] not in visited:
            grid = explore(grid,i,j-1,k,visited,count)
        if j+1 < grid.shape[1] and [i,j+1] not in visited:
             grid = explore(grid,i,j+1,k,visited,count)
        return grid
    
grid = np.array(read_input('iput.txt'))
final_grid = grid.copy()

score = 0
lower_points = []
for row in range(grid.shape[0]):
    for column in range(grid.shape[1]):
        is_low = True
        if row - 1 >= 0:
            if grid[row,column] >= grid[row-1,column]:
                is_low = False
        if column - 1 >= 0:
            if grid[row,column] >= grid[row,column-1]:
                is_low = False
        if row + 1 < grid.shape[0]:
            if grid[row,column] >= grid[row+1,column]:
                is_low = False
        if column + 1 < grid.shape[1]:
            if grid[row,column] >= grid[row,column+1]:
                is_low = False
        if is_low:
            score += (grid[row,column] + 1)
            lower_points.append([row,column])
        else:
            if grid[row,column] != 9:
                final_grid[row,column] = -1
            
print('solution part A:', score)

for k,point in enumerate(lower_points):
    final_grid  = explore(final_grid,point[0],point[1],k)
    
result = {}
for row in range(final_grid.shape[0]):
    for column in range(final_grid.shape[1]):
        if final_grid[row,column]!=9:
            if final_grid[row,column] not in result:
                result[final_grid[row,column]] = 1
            else:
                result[final_grid[row,column]] += 1
                
print('solution part B:', np.prod(sorted(result.values())[-3:]))
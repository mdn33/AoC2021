def read_input(file_name):
    grid = []
    with open(file_name) as f:
        for line in f:
            v = [digit for digit in line.strip()]
            grid.append(v)
        return grid
    
    
def move(grid):
    
    count = 0
    
    while(1):
        f_horizontal = False
        can_move = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '>':
                    if grid[i][(j+1)%len(grid[0])] == '.':
                        can_move.append((i,j))
                        
        if len(can_move) > 0:
            f_horizontal = True
            
        for cucumber in can_move:
            grid[cucumber[0]][cucumber[1]] = '.'
            grid[cucumber[0]][(cucumber[1]+1)%len(grid[0])] = '>'

        can_move = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'v':
                    if grid[(i+1)%len(grid)][j] == '.':
                        can_move.append((i,j))

        if len(can_move) == 0 and f_horizontal == False:
            return count+1

        for cucumber in can_move:
            grid[cucumber[0]][cucumber[1]] = '.'
            grid[(cucumber[0]+1)%len(grid)][cucumber[1]] = 'v'
            
        count += 1

grid = read_input('input.txt')
count = move(grid)
count

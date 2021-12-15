import numpy as np
import networkx as nx

def read_input(file_name):
    grid = []
    with open(file_name) as f:
        for line in f:
            v = [int(digit) for digit in line.strip()]
            grid.append(v)
        return grid
    
def shortest_path(G,grid):
    total = 0
    for e in G.edges():
        G[e[0]][e[1]]['weight'] = grid[e[1][0]][e[1][1]]
    path = nx.dijkstra_path(G, (0,0), (len(grid)-1, len(grid[0])-1))
    for e in path:
        total += grid[e[0]][e[1]]
    total -= grid[0][0]
    return total

grid = read_input('input.txt')
G=nx.grid_2d_graph(len(grid), len(grid[0]),create_using=nx.DiGraph)


print('total:', shortest_path(G,grid))


grid = np.array(grid)
complete_grid = []
for i in range(5):
    p = []
    for j in range(5):
        grid_new = grid + i + j
        grid_new[grid_new>9] -= 9
        p.append(grid_new) 
    complete_grid.append(p)      
complete_grid = np.block(complete_grid).reshape((len(grid)*5,len(grid)*5))

G=nx.grid_2d_graph(len(grid)*5, len(grid)*5,create_using=nx.DiGraph)
print('total:', shortest_path(G,complete_grid))

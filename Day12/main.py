import numpy as np

def read_graph(file_name):
    graph = {}
    with open(file_name, "r") as fd:
        for line in fd:
            point_a = line.strip().split('-')[0].strip()
            point_b = line.strip().split('-')[1].strip()

            if point_a not in graph:
                graph[point_a] = [point_b]
            else:
                graph[point_a].append(point_b)

            if point_a != 'start':
                if point_b not in graph:
                    graph[point_b] = [point_a]
                else:
                    graph[point_b].append(point_a)

        graph['end'] = []
        
    return graph

def count_occurrences(array,char):
    
    if char not in array:
        return True
    else:
        u, c = np.unique(np.array(array)[np.char.islower(np.array(array))], return_counts=True)
        if len(u[c > 1]) > 0:
            return False
        else:
            return True 
        
def visit(graph,point,visited,count):
        
    visited.append(point)
    if point == 'end':
        return count + 1
    
    for near_point in graph[point]:
        if near_point!='start' and (near_point.isupper() or (near_point.isupper() == False and count_occurrences(visited,near_point))):
            visited_previous = visited.copy()
            count = visit(graph,near_point,visited,count)
            visited = visited_previous
    return count

file_name = 'iput.txt'
graph = read_graph(file_name)
count = visit(graph,'start',[],0)
print('Answer Part B:', count)
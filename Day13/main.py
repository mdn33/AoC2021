import numpy as np

def read_dots (file_name):
    
    dots_list = []
    folds = []
    with open(file_name, "r") as fd:
        for line in fd:
            line = line.strip()
            if line == '':
                continue
            if 'fold along' in line.strip():
                value = int(line.split('=')[1])
                direction = line.split('=')[0].split('fold along')[1].strip()
                folds.append([direction,value])
            else:
                point_a = int(line.strip().split(',')[0].strip())
                point_b = int(line.strip().split(',')[1].strip())
                dots_list.append([point_a,point_b])

        dots_list = np.array(dots_list)
        shape_x = int(dots_list[:,0].max() + 1)
        shape_y = int(dots_list[:,1].max() + 1)
        paper = np.zeros((shape_y,shape_x))
    
    for point in dots_list:
        paper[point[1],point[0]]=1
        
    return paper,folds

def fold_paper(paper,direction,line):
    if direction == 'y':
        first_part = paper[:line,:]
        second_part = np.flip(paper[line+1:,:],axis = 0)
        paper = first_part + np.pad(second_part,((first_part.shape[0] - second_part.shape[0],0),(0,0))) 
    else:
        first_part = paper[:,:line]
        second_part = np.flip(paper[:,line+1:],axis = 1)
        paper = first_part + np.pad(second_part,((0,0),(first_part.shape[1] - second_part.shape[1],0)))  
    return paper


paper, folds = read_dots('iput.txt')
for fold in folds:
    paper = fold_paper(paper,fold[0],fold[1])

count = 0
for row in range(paper.shape[0]):
    for column in range(paper.shape[1]):
        if paper[row,column] > 0:
            count += 1
            paper[row,column] = 1
        
            
print('Answer:', count)
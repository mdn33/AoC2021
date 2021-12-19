import json
from math import *


def split(nested,found):
    
    if isinstance(nested, int):
            if nested > 10 and found[0] == 0:
                split_left = floor(nested/2)
                split_right = ceil(nested/2)
                found[0] = 1
                return [split_left,split_right]
            else:
                return nested
            
    elif (isinstance(nested, list) and any(isinstance(i, list) for i in nested) == False):
        return [nested[0],nested[1]]
    
    else:
        split_left = split(nested[0],found)
        split_right = split(nested[1],found)
            
        return [split_left,split_right]

def explode(nested,found,level):
    
    if isinstance(nested, int):
        return
    elif level == 4:
        print(nested)
        return
        
    else:
        split_left =  explode(nested[0],found,level+1)
        split_right = explode(nested[1],found,level+1)
            
        #return [split_left,split_right]
        
input_string = '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'
input_string = json.loads(input_string)
n = parse_input(input_string)
splitted = [0]
reduced_number = split(input_string,splitted)
import json
from math import *

class snailfish():
    def __init__(self):
        self.left = None
        self.right = None
        
    def set_left(self,snail):
        self.left = snail
        
    def set_right(self, snail):
        self.right = snail
        
    def split(self):
        ## aggiungi for per gli elementi della lista
        if isinstance(self.left, int) and self.left > 10:
            splitted = snailfish()
            splitted.left = floor(self.left/2)
            splitted.right = ceil(self.left/2)
            self.left = splitted
            return True
        elif self.left.split():
            return True
        elif isinstance(self.right, int) and self.right > 10:
            splitted = snailfish()
            splitted.left = floor(self.right/2)
            splitted.right = ceil(self.right/2)
            self.right = splitted
            return True
        elif self.right.split():
            return True
        

def parse_input(list_int):
    
    n = snailfish()
    
    if (isinstance(list_int[0], list) and any(isinstance(i, list) for i in list_int[0]) == False) or isinstance(list_int[0], int):
        n.set_left(list_int[0])
    else:
        n.set_left(parse_input(list_int[0]))

    if (isinstance(list_int[1], list) and any(isinstance(i, list) for i in list_int[1]) == False) or isinstance(list_int[1], int):
        n.set_right(list_int[1])
    else:
        n.set_right(parse_input(list_int[1]))
        
    return n

input_string = '[[[1,2],15], 20]'
input_string = json.loads(input_string)
n = parse_input(input_string)
n.split()
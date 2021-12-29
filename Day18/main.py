import json
import numpy as np
from math import *
from itertools import permutations

class snailfish_number():
    
    def __init__(self, string):
        self.levels = []
        self.numbers = []
        
        inp_list = json.loads(string)
        self.initialize(inp_list,self.levels,-1,self.numbers)
        
        
    def initialize(self,inp_list,res,level,numbers):
    
        if isinstance(inp_list, int):
            res.append(level)
            numbers.append(inp_list)
            return

        self.initialize(inp_list[0],res,level+1,numbers)
        self.initialize(inp_list[1],res,level+1,numbers)
     
    def explode(self):
    
        couple = -1
        for i in range(len(self.levels)):
            if self.levels[i] == 4:
                couple = i
                break

        if couple != -1:
            if couple-1 >= 0:
                self.numbers[couple-1] += self.numbers[couple]
            if couple+2 < len(self.numbers):
                self.numbers[couple+2] += self.numbers[couple+1]

            self.numbers[couple] = 0
            self.levels[couple] -= 1
            self.numbers.pop(couple+1)
            self.levels.pop(couple+1)
            return True
        else:
            return False
        
    def split(self):

        couple = -1
        for i in range(len(self.numbers)):
            if self.numbers[i] >= 10:
                couple = i
                break

        if couple != -1:
            split_left = floor(self.numbers[couple]/2)
            split_right = ceil(self.numbers[couple]/2)

            self.numbers[couple] = split_left
            self.numbers.insert(couple+1,split_right)

            self.levels[couple] += 1
            self.levels.insert(couple+1,self.levels[couple])
            return True
        else:
            return False

    def reduce(self):
        while(1):
            if self.explode() == False:
                if self.split() == False:
                    break
                    
    def get_magnitude(self):
        
        while len(self.levels) > 1:
            for i in range(len(self.levels)):
                if i+1 < len(self.levels):
                    if self.levels[i] == self.levels[i+1]:
                        magnitude = 3*self.numbers[i] + 2*self.numbers[i+1]
                        self.numbers[i] = magnitude
                        self.levels[i] -= 1
                        self.levels.pop(i+1)
                        self.numbers.pop(i+1)
                        break
                        
        return self.numbers[0]
                        
    def add(self,snailfish_numb):
        self.levels.extend(snailfish_numb.levels)
        self.numbers.extend(snailfish_numb.numbers)
        self.levels = list(map(lambda x:x+1, self.levels))
        self.reduce()

        
#Part 1    
with open('input.txt') as  fd:
    
    inp_list = fd.readline().strip()
    s = snailfish_number(inp_list)
    
    lines = fd.read().splitlines()
    for line in lines:
        s_new = snailfish_number(line)
        s.add(s_new)
            
print('Answer Part A:', s.get_magnitude())


#Part 2
snail = []
max_magn = -1

with open('input.txt') as  fd:
    lines = fd.read().splitlines()
    for line in lines:
        snail.append(line)
        
for p in list(permutations([i for i in range(len(snail))],2)):
    
    s1 = snailfish_number(snail[p[0]])
    s2 = snailfish_number(snail[p[1]])
    s1.add(s2)
    m = s1.get_magnitude()
    if m > max_magn:
        max_magn = m
          
print('Answer Part B', max_magn)

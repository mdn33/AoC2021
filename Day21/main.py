import itertools
import functools

class player():
    
    def __init__(self, position):
        self.score = 0
        self.position = position
    
    def move(self,dice):
        movements = dice.roll() + dice.roll() + dice.roll()
        self.position = (self.position + movements)
        if self.position > 10:
            if self.position%10 == 0:
                self.position = 10
            else:
                self.position = self.position%10
        self.score += self.position
    
    def check_win(self):
        return self.score >= 1000

    
class dice():
    
    def __init__(self):
        self.score = 1
        self.counter = 0
        
    def roll(self):
        score = self.score
        self.score += 1
        if self.score > 100:
            self.score = self.score%100
        self.counter += 1
        return score
    
    def get_counter(self):
        return self.counter
    
    
p1 = player(2)
p2 = player(1)
d = dice()

while(True):
    p1.move(d)
    if p1.check_win():
        print('Player 1 wins')
        loser = p2
        break
    p2.move(d)
    if p2.check_win():
        print('Player 2 wins')
        loser = p1
        break
        
print(f'dice has been rolled {d.get_counter()} times')
print(f'Answer part 1 {d.get_counter()*loser.score}')


@functools.lru_cache(maxsize=None)
def play(p1,s1,p2,s2):
    w1 = 0
    w2 = 0
    for m1,m2,m3 in itertools.product((1,2,3),(1,2,3),(1,2,3)):
        p1c = p1 + m1 + m2 + m3
        if p1c > 10:
            if p1c%10 == 0:
                p1c = 10
            else:
                p1c = p1c%10
        s1c = s1 + p1c
        if s1c >= 21:
            w1 += 1
        else:
            w2c, w1c = play(p2,s2,p1c,s1c)
            w1 += w1c
            w2 += w2c
    return w1,w2

print('Answer Part 2:', max(play(2,0,1,0)))

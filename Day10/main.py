map_closing = {"(": ")", "{": "}", "[": "]", "<": ">"}
points = {")": 3, "]": 57, '}': 1197, '>':25137}
points_auto = {")": 1, "]": 2, '}': 3, '>':4}

total = 0
scores_list = []

with open('iput.txt', "r") as fd:
    for x in fd:
        x = x.strip()
        expected = []
        complete_score = 0
        for i,element in enumerate(x):
            if element in map_closing.keys():
                expected.append(map_closing[element]) 
            if i == len(x)-1:  
                if element == expected[-1]:
                    expected.pop()
                for c in list(reversed(expected)): complete_score = complete_score*5 + points_auto[c]
                scores_list.append(complete_score)
            elif element not in map_closing.keys():
                closed = expected.pop()
                if element != closed:
                    total += points[element]
                    break
                

print('Answer part A:', total)
print('Answer part B:', sorted(scores_list)[int(len(scores_list)/2)])
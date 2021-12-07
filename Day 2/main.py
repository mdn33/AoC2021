

if __name__ == '__main__':
    position = {"horizontal": 0, "depth":0,"aim":0}
    file_name = 'input.txt'
    with open(file_name, "r") as fd:
            for row in fd:
                direction = row.strip().split(' ')[0]
                quanity = int(row.strip().split(' ')[1])
                if  direction == 'forward':
                    position['horizontal'] += int(quanity)
                    position['depth'] += int(int(quanity)*position['aim'])
                elif direction == 'down':
                    position['aim'] += int(quanity)
                elif direction == 'up':
                    position['aim'] -= int(quanity)
              
    print("solution:", position['horizontal']*position['depth'])
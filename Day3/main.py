import numpy as np

def to_int(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | int(bit)
    return out

def reduce(bitlist, mode):
    
    result = bitlist
    j = 0
    while len(result) > 1 and j<result.shape[1]: 
        counts = {"0": 0,"1":0}
        rows = {"0":[], "1":[]}
        for i in range(0,result.shape[0]):
            counts[result[i,j]] = counts[result[i,j]] + 1
            rows[result[i,j]].append(i)
        if mode == 1:
            if counts["0"] > counts["1"]:
                result = result[rows["1"],:]
            else:
                result = result[rows["0"],:]
        elif mode == 0:
            if counts["0"] <= counts["1"]:
                result = result[rows["1"],:]
            else:
                result = result[rows["0"],:] 
        #print(result,j)
        j = j + 1   
    return result

bits = []

if __name__ == '__main__':
    with open('input.txt') as file:
        for line in file:
            bits.append([bit for bit in line.rstrip('\n')])
    bits = np.array(bits)

    ox = reduce(bits,0)
    co2 = reduce(bits,1)
    result = to_int(co2[0])*to_int(ox[0])
    print('oxygen generator rating:', ox[0], "= decimal", to_int(ox[0]))
    print('CO2 scrubber rating', co2[0], "= decimal", to_int(co2[0]))
    print('life support rating:', result)
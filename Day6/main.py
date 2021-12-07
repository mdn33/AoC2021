def fill_with_zeros(initial_state_dict):
    v = initial_state_dict
    for i in range(0,9):
        if i not in v:
            v[i] = 0
    return v

def read_file(filename):
  initial_state_dict = {}
  with open(filename, "r") as fd:
    for v in fd.readlines()[0].split(','):
        timer = int(v)
        if timer not in initial_state_dict:
            initial_state_dict[timer] = 1
        else:
            initial_state_dict[timer] += 1
    return   initial_state_dict

def solve(initial_state_dict,number_of_days):
    initial_state_dict = fill_with_zeros(initial_state_dict)
    for day in range(1,number_of_days + 1):
        final_state_dict = {}
        for j in range(8,0,-1):
            final_state_dict[j-1] = initial_state_dict[j]
        
        final_state_dict = fill_with_zeros(final_state_dict)
        final_state_dict[6] +=  initial_state_dict[0]
        final_state_dict[8] +=  initial_state_dict[0]

        initial_state_dict = final_state_dict

    return sum(initial_state_dict.values())

if __name__ == '__main__':
    number_of_days = 256
    solution = solve(read_file("input.txt"),number_of_days)
    print(f'fishes after {number_of_days}: {solution}')
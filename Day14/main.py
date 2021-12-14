from collections import defaultdict

def read(file_name):
    mapping = {}
    with open(file_name, "r") as fd:
        for line in fd:
            line = line.strip()
            if line == '':
                continue
            if '->' in line.strip():
                a = line.split('->')[0].strip()
                b = line.split('->')[1].strip()
                mapping[a] = b
            else:
                sequence = line
    return sequence,mapping

def create_pairs(sequence):
    pairs = {}
    for i in range(len(sequence)):
        pair = sequence[i:i+2]
        if len(pair) == 2:
            if pair not in pairs:
                pairs[pair] = 1
            else:
                pairs[pair] += 1
    return pairs

def compute_polimery(step,mapping,pairs,char_counts):
    for i in range(step):
        final_sequence = defaultdict(int)
        for pair,mapped in mapping.items():
            if pair in pairs:
                final_sequence[pair[0]+mapped] += pairs[pair]
                final_sequence[mapped+pair[1]] += pairs[pair]   
                char_counts[mapped] += pairs[pair]
        pairs = final_sequence
    return sorted(char_counts.items(), key=lambda k_v: k_v[1], reverse=True)

nstep = 1
sequence,mapping = read('iput.txt')
pairs = create_pairs(sequence)
char_counts = defaultdict(int)
for c in sequence: char_counts[c] += 1
char_counts = compute_polimery(nstep,mapping,pairs,char_counts)
print('Result: ', char_counts[0][1] - char_counts[-1][1])
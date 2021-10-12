with open("UDify-Scores.tsv", "rt") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    lines[idx] = line.strip().split('\t')

sizes = [line[9] for line in lines]

print(sizes.count('0'))
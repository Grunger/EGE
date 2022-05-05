import sys

data = sys.stdin.read().strip().split('\n')
for i in range(len(data)):
    data[i] = sorted([int(j) for j in data[i].split()])
k = 0
for line in data:
    if line[0] == line[1] and line[2] == line[3] and line[4] == line[5]:
        k += 1
print(k)

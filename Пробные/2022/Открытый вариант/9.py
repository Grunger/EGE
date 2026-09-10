from sys import stdin


k = 0
for line in stdin.read().strip().split('\n'):
    line = sorted(map(int, line.split('\t')))
    if (line[0] + line[4]) ** 2 > line[1] ** 2 + line[2] ** 2 + line[3] ** 2:
        k += 1
print(k)

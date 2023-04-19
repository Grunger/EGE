f = open('26.txt')
n = int(f.readline())
d = dict()
for line in f:
    row, col = map(int, line.split())
    d[row] = d.get(row, []) + [col]
for i in d:
    d[i].sort()
for row in sorted(d, reverse=True):
    for i in range(len(d[row]) - 1):
        if d[row][i + 1] - d[row][i] == 14:
            print(row, d[row][i] + 1)
            exit(0)

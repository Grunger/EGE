f = open('26_apr_2022.txt')
n = int(f.readline())
d = {}
for line in f:
    row, col = map(int, line.split())
    d[row] = d.get(row, []) + [col]
for row in sorted(d):
    d[row].sort()
    for i in range(len(d[row]) - 1):
        if d[row][i + 1] - d[row][i] == 14:
            print(row, d[row][i] + 1)

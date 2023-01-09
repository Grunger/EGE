f = open('26_t.txt')
n = int(f.readline())
d = dict()
for line in f:
    row, col = map(int, line.split())
    if row in d:
        d[row].append(col)
    else:
        d[row] = [col]
for item in d:
    d[item].sort()

max_r, min_c = 0, 10**9
for row in sorted(d):
    for i in range(len(d[row]) - 1):
        if d[row][i + 1] - d[row][i] == 3:
            if row > max_r:
                max_r = row
                min_c = d[row][i] + 1
print(max_r, min_c)



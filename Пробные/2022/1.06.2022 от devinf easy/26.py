f = open('26.txt')
n = int(f.readline())
d = dict()
for i in range(n):
    row, place = map(int, f.readline().split())
    d[row] = d.get(row, []) + [place]
r = 0
m = 0
for row in sorted(d):
    d[row].sort()
    for i in range(len(d[row]) - 1):
        if d[row][i + 1] - d[row][i] == 2 and d[row][i] - 1 not in d and d[row][i + 1] + 1 not in d:
            if d[row][i] > m:
                m = d[row][i + 1]
                r = row
print(r, m)

# 24566 91982

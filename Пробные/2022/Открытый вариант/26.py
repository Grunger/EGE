f = open('107_26.txt')
n = int(f.readline())
d = dict()
for i in range(n):
    row, col = map(int, f.readline().split())
    if row in d:
        d[row].append(col)
    else:
        d[row] = [col]
for row in sorted(d):
    d[row].sort()
    for a, b in zip(d[row], d[row][1:]):
        if b - a == 14:
            print(row, a, b)

f = open('26.txt')
n = int(f.readline())
d = dict()
for i in range(n):
    r, c = map(int, f.readline().split())
    if r not in d:
        d[r] = []
    d[r].append(c)
for r in sorted(d):
    d[r].sort()
    for i in range(len(d[r]) - 1):
        if d[r][i + 1] - d[r][i] == 3:
            print(r, d[r][i] + 1)
            break
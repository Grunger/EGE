f = open('26_apple.txt')
n = int(f.readline())
d = dict()
for i in range(n):
    row, col = map(int, f.readline().split())
    d[row] = d.get(row, [])
    d[row].append(col)
for i in d:
    print(i, ':', d[i])
print('-' * 20)

for row in sorted(d):
    d[row].sort()
    for i in range(len(d[row]) - 1):
        if d[row][i + 1] - d[row][i] == 25 + 1:
            print(row, d[row][i] + 1)
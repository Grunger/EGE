f = open('26_apple.txt')
n = int(f.readline())
d = dict()
for i in range(n):
    row, col = map(int, f.readline().split())
    d[row] = d.get(row, [])
    d[row].append(col)
print(d)

places = dict()
with open('26.txt') as f:
    n = int(f.readline())
    for i in range(n):
        row, col = map(int, f.readline().split())
        places[row] = places.get(row, []) + [col]
step = 5
for x in sorted(places.keys()):
    d = sorted(places[x])
    for i in range(len(d) - step + 1):
        if d[i + step - 1] - d[i] <= step - 1:
            print(x, d[i + step - 1])

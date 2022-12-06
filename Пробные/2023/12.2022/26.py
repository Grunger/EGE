f = open('26.txt')
n = int(f.readline())
data = sorted([int(i) for i in f])
mx = 0
mx_start = 0
for start in range(n):
    last = data[start]
    k = 1
    for nn in range(start + 1, n):
        if data[nn] - last >= 8:
            k += 1
            last = data[nn]
    if k > mx:
        mx = k
        mx_start = data[start]
    elif k == mx:
        mx_start = data[start]
print(mx, mx_start)

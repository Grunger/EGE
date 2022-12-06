def od(a, b):
    k = 2
    while k ** 2 <= min(a, b):
        if a % k == 0 and b % k == 0:
            return True
        k += 1
    return False


f = open('26_5242.txt')
nn = int(f.readline())
print(nn)
boxes = sorted([int(i) for i in f])
mx = 0
mx_start = 0
for start in range(nn):
    if start % 100 == 0:
        print(start)
    k = 1
    last = boxes[start]
    for n in range(start + 1, nn):
        if boxes[n] - last >= 3 and od(boxes[n], last):
            last = boxes[n]
            k += 1
    if k > mx:
        mx = k
        mx_start = boxes[start]
    elif k == mx:
        mx_start = boxes[start]
print(mx, mx_start)

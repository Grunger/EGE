f = open('26_3.txt')
n = int(f.readline())
boxes = sorted([int(i) for i in f])

mx = 0
mx_start = 0
for start in range(len(boxes)):
    k = 0
    last = start
    for i in range(start + 1, len(boxes)):
        if boxes[i] - last >= 3:
            k += 1
            last = boxes[i]
    if k >= mx:
        mx = k
        mx_start = boxes[start]
print(mx, mx_start)

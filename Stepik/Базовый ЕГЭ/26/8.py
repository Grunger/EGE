f = open('26_07.txt')
n = int(f.readline())
boxes = [int(i) for i in f]
boxes.sort()

mx = 854
for start in range(100):
    k = 1
    last = boxes[start]
    for i in range(n):
        if boxes[i] >= last + 11:
            k += 1
            last = boxes[i]
    if k == mx:
        print(k)
        print(boxes[start])

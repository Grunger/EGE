f = open('26_3.txt')
n = int(f.readline())
boxes = [int(i) for i in f]
boxes.sort()
k = 1
last = boxes[0]
for i in range(n):
    if boxes[i] >= last + 3:
        k += 1
        last = boxes[i]
print(k)
print(boxes[4])
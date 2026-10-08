f = open('26.txt')
n = int(f.readline())
boxes = sorted({int(f.readline()) for i in range(n)})
mx = 0
box = 0
for i in range(len(boxes)):
    pack = [boxes[i]]
    for i in range(len(boxes)):
        if boxes[i] >= pack[-1] + 3:
            pack.append(boxes[i])
    if len(pack) >= mx:
        mx = len(pack)
        box = pack[0]
print(mx, box)


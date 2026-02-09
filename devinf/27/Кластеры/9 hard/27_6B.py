from math import dist, sqrt

def center(cluster):
    best = None
    bestsm = float("inf")

    for x,y in cluster:
        s = 0
        for x1, y1 in cluster:
            s += sqrt( ((x - x1)**2) + ( (y - y1)**2) )
        if s < bestsm:
            bestsm = s
            best = [x, y]

    return best


f = open("27-Б.txt")


data = []
for line in f:
    x,y = [float(x) for x in line.replace(",",".").split()]
    data.append([x,y])
print(len(data))


clusters = []
while data:
    clusters.append([data.pop(0)])

    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p, p1) < 0.1]
        clusters[-1].extend(sosedi)
        for p1 in sosedi:
            data.remove(p1)

    print(len(clusters[-1]))

print(center(clusters[0]))
print(center(clusters[1]))
print(center(clusters[2]))



print(int(abs(((center(clusters[0])[0] + center(clusters[1])[0] + center(clusters[2])[0]) / 3) * 10000)))
print(int(abs(((center(clusters[0])[1] + center(clusters[1])[1] + center(clusters[2])[1]) / 3) * 10000)))

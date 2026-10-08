data = [i.split() for i in open('6.txt').readlines()]
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = float(data[i][j])
print(data)
k = 0
for point in data:
    x, y = point
    if x ** 2 + y ** 2 < 1 and (y > -x or y < x):
        print(point)
        k += 1
print(k)

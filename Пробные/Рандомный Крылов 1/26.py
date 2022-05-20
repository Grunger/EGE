f = open('26.txt')
s, n = map(int, f.readline().split())
print(s)
data = sorted(map(int, f.readlines()))
print(data)
sm = 0
for i in range(len(data)):
    sm += data[i]
    if sm > s:
        print(i)
        print(sm)
        print(data[i])
        print(data[i] + s - (sm - data[i]))
        break
print(80 in data)
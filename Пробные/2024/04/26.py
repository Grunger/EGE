f = open('26.txt')
n, m = map(int, f.readline().split())
pipes = sorted([int(i) for i in f], reverse=True)
k = 0
way = [pipes[0]]
i = 1
mx = 0
print(pipes)
while i < n:
    if way[-1] - pipes[i] <= 3:
        way.append(pipes[i])
    else:
        if len(way) >= m:
            # print(len(way), way[:m][-1])
            mx = max(mx, way[:m][-1])
            if mx == 311:
                print(way[:5], way[m:])
        way = [pipes[i]]
    i += 1
print(mx)

f = open('26.txt')
n, m = map(int, f.readline().split())

pipes = sorted([int(i) for i in f], reverse=True)
way = [pipes[0]]
i = 1
mx = 0
# print(pipes)
while i < n:
    if way[-1] - pipes[i] <= 11:
        way.append(pipes[i])
    else:
        # print(way)
        if len(way) >= m:
            # print(len(way), way)
            while len(way) >= m and way[m - 1] == way[m]:
                way.pop(0)
            way = way[:m]
            print(way[-1], way[0])
        way = [pipes[i]]
    i += 1
if len(way) >= m:
    # print(len(way), way)
    while len(way) >= m and way[m - 1] == way[m]:
        way.pop(0)
    way = way[:m]
    print(way[-1], way[0])

# 1745 1992

import sys
from time import time

data = sys.stdin.readlines()
for i in range(len(data)):
    data[i] = [int(j) for j in data[i].split()]
# bfs
n = len(data)
#   sum  y  x
s = [(0, 0, 0)]
ans = set()
k = 0
start = time()
while s:
    k += 1
    if k % 10000000 == 0:
        print(k, len(s))
    curr = s.pop()
    if curr[1] == curr[2] == n - 1:
        # последняя ячейка
        ans.add(curr[0])
        continue
    if curr[1] == n - 1:
        # первый ряд. Идем направо
        if data[curr[1]][curr[2] + 1] > data[curr[1]][curr[2]]:
            delta = 1
        else:
            delta = 2
        s.append((curr[0] + delta, curr[1], curr[2] + 1))
    elif curr[2] == n - 1:
        # первый столбец. Идем вниз
        if data[curr[1] + 1][curr[2]] > data[curr[1]][curr[2]]:
            delta = 1
        else:
            delta = 2
        s.append((curr[0] + delta, curr[1] + 1, curr[2]))
    else:
        if data[curr[1]][curr[2] + 1] > data[curr[1]][curr[2]]:
            delta = 1
        else:
            delta = 2
        s.append((curr[0] + delta, curr[1], curr[2] + 1))
        if data[curr[1] + 1][curr[2]] > data[curr[1]][curr[2]]:
            delta = 1
        else:
            delta = 2
        s.append((curr[0] + delta, curr[1] + 1, curr[2]))
print(sorted(ans))
print(min(ans))
print(max(ans))
print(f'Time: {time() - start}')

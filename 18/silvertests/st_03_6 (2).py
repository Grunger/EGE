import sys
from time import time

data = sys.stdin.readlines()
for i in range(len(data)):
    data[i] = [int(j) for j in data[i].split()]
# bfs
n = len(data)
s = [(data[0][0], 0, 0)]
ans = set()
stock = 600
k = 0
start = time()
while s:
    k += 1
    if k % 10000000 == 0:
        print(k, len(s))
    curr = s.pop()
    if stock - curr[0] <= 0:
        continue
    if curr[1] == curr[2] == n - 1:
        ans.add(curr[0])
        continue
    if curr[1] == n - 1:
        s.append((curr[0] + data[curr[1]][curr[2] + 1], curr[1], curr[2] + 1))
    elif curr[2] == n - 1:
        s.append((curr[0] + data[curr[1] + 1][curr[2]], curr[1] + 1, curr[2]))
    else:
        s.append((curr[0] + data[curr[1]][curr[2] + 1], curr[1], curr[2] + 1))
        s.append((curr[0] + data[curr[1] + 1][curr[2]], curr[1] + 1, curr[2]))
print(sorted(ans))
print(stock - min(ans))
print(stock - max(ans))
print(f'Time: {time() - start}')

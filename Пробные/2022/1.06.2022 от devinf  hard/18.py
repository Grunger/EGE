import sys
from time import time


def score(b, a):
    if a > b:
        return 3
    if a == b:
        return 1
    return 0


data = sys.stdin.readlines()
for i in range(len(data)):
    data[i] = [int(j) for j in data[i].split()]
# bfs
n = len(data)
#  текущий счет, координата y, координата x
s = [(0, 0, 0)]
ans = set()

k = 0
start = time()
while s:
    k += 1
    if k % 10000000 == 0:
        print(k, len(s))
    curr = s.pop()
    y, x = curr[1], curr[2]
    if curr[1] == curr[2] == n - 1:
        ans.add(curr[0])
        continue
    if curr[1] == n - 1:
        # первая строка. шагаем только вправо
        s.append((curr[0] + score(data[y][x], data[y][x + 1]), y, x + 1))
    elif curr[2] == n - 1:
        # первый столец. шагаем только вниз
        s.append((curr[0] + score(data[y][x], data[y + 1][x]), y + 1, x))
    else:
        s.append((curr[0] + score(data[y][x], data[y][x + 1]), y, x + 1))
        s.append((curr[0] + score(data[y][x], data[y + 1][x]), y + 1, x))
print(sorted(ans))
print(min(ans))
print(max(ans))
print(f'Time: {time() - start}')

import sys
from itertools import permutations


data = sys.stdin.read().strip().split('\n')
for i in range(len(data)):
    data[i] = [int(a) for a in data[i].split('\t')]
k = 0
for item in data:
    if all(a[0] ** 3 + a[1] ** 3 > (a[2] + a[3] + a[4]) ** 2
           for a in permutations(item)):
        k += 1
print(k)


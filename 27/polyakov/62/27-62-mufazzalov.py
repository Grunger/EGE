# Автор: Д. Муфаззалов

import bisect
F = open("27-62.txt")

k = 101
ans = 2
d = 10**8 + 1
b = [[[0, d] for j in range(i)] for i in range(k)]
c = [[{0: 0, d: 0} for j in range(i)] for i in range(k)]

for i in range(int(F.readline())):
  n = int(F.readline())
  for j in range(1, k):
    r = n % j
    bisect.insort(b[j][r], n)
    z, c[j][r][n] = b[j][r].index(n) - 1, 1
    for q in range(2):
      r1, r2 = b[j][r][z], b[j][r][z + 1]
      if r1 + j*c[j][r][r1] == r2:
        c[j][r][r1] += c[j][r][r2]
        ans = max(ans, c[j][r][r1])
        c[j][r].pop(r2), b[j][r].pop(z + 1)
      else:
        z += 1

print(ans)

from collections import defaultdict

with open("27.txt") as F:
  n = int(F.readline())
  count = defaultdict( int, {0: 1} )
  current, count57 = 0, 0
  for i, x in enumerate(map(int, F)):
    if i >= n: break
    current += (x % 5 == 0) - (x % 7 == 0)
    count57 += count[current]
    count[current] += 1

print( count57 )

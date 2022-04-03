#with open('27.txt') as F:
with open('27-97b.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for i in range(N) ]

count = 0
tailCount = [1] + [0]*(K-1)
totalSum = 0
for x in data:
  totalSum += x
  r = totalSum % K
  count += tailCount[r]
  tailCount[r] += 1

print( count )
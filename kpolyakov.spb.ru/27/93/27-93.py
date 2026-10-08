def isSpecNumber(x):
  return x < 0 and abs(x) % 10 == 3

f = open('27-93a.txt')
N, K = map( int, f.readline().split() )

maxSum = -10**20

sumTotal = 0
minTails = [10**20]*(K+1)
minTails[K] = 0
for _ in range(N):

  x = int(f.readline())
  sumTotal += x

  if isSpecNumber(x):
    for i in range(K):
      minTails[i] = minTails[i+1]
    minTails[K] = sumTotal

  if sumTotal - minTails[0] > maxSum:
    maxSum = sumTotal - minTails[0]

  minTails[K] = min( minTails[K], sumTotal )

  # print(f"{_}, {x:2}, {sumTotal:2},  {maxSum:2}, {minTails}")

f.close()

print( maxSum )

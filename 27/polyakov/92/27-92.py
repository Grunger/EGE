def isSpecNumber(x):
  return x > 0 and x % 2 == 0

f = open('27-92b.txt')
N = int(f.readline())

maxSum = -10**20

sumTotal = 0
minTails = [10**20]*2

for _ in range(N):

  x = int(f.readline())
  sumTotal += x

  if isSpecNumber(x):
    minTails[0] = minTails[1]
    minTails[1] = sumTotal

  if sumTotal - minTails[0] > maxSum:
    maxSum = sumTotal - minTails[0]

  minTails[1] = min( minTails[1], sumTotal )

  # print(f"{x:2}, {sumTotal:2}, {maxSum:2}, {minTails}")

f.close()

print( maxSum )

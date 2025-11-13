def isSpecNumber( x ):
  x = -x
  if x <= 0: return False
  while x:
    if x % 5 == 1: return False
    x //= 5
  return True

f = open('27-90b.txt')
#f = open('27.txt')
n, K, D = map(int, f.readline().split())

maxSum = -10**20
minTails = [ [10**20]*D for i in range(K) ]

sumTotal = 0
count = 0
for i in range(n):

  x = int(f.readline())

  sumTotal += x
  rSum = sumTotal % D

  if isSpecNumber(x):
    count += 1

  r = count % K
  if r == 0 and rSum == 0 and sumTotal > maxSum:
    maxSum = sumTotal

  if minTails[r][rSum] != 10**20 and sumTotal - minTails[r][rSum] > maxSum:
    maxSum = sumTotal - minTails[r][rSum]

  minTails[r][rSum] = min( minTails[r][rSum], sumTotal )

  #print( x, maxSum )

f.close()

print( maxSum )

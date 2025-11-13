def isSpecNumber( x ):
  x = -x
  if x <= 0: return False
  s = 0
  while x:
    s += x % 3
    x //= 3
  return s == 12

f = open('27-91b.txt')
#f = open('27.txt')
n, K, D = map(int, f.readline().split())

maxSum = -10**20
minTails = [ [10**20]*D for i in range(K) ]

sumTotal = 0
count, countSpec = 0, 0
for i in range(n):

  x = int(f.readline())

  sumTotal += x

  count += 1
  r = count % D

  if isSpecNumber(x):
    countSpec += 1
  rSpec = countSpec % K

  if rSpec == 0 and r == 0 and sumTotal > maxSum:
    maxSum = sumTotal

  if minTails[rSpec][r] != 10**20 and sumTotal - minTails[rSpec][r] > maxSum:
    maxSum = sumTotal - minTails[rSpec][r]

  minTails[rSpec][r] = min( minTails[rSpec][r], sumTotal )

  #print( x, maxSum )

f.close()

print( maxSum )

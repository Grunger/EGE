K, M = 37, 73

F = open("27.txt")
N = int( F.readline() )

tailSum = [ [0] + [None]*(K-1) ]
for i in range(M-1):
  tailSum.append( [None]*K )

tailLen = [[0]*K for i in range(M)]

maxSum, minLen = 0, 0
totalSum = 0
r = 0

for i in range(1,N+1):
  x = int( F.readline() )
  totalSum += x
  ri = x % M

  if tailSum[ri][r] == None:
    tailSum[ri][r] = totalSum
    tailLen[ri][r] = i

  r0 = (M - ri) % M
  r = totalSum % K
  if tailSum[r0][r] != None:
    curSum = totalSum - tailSum[r0][r]
    curLen = i - tailLen[r0][r] + 1
    if curSum > maxSum or \
       (curSum == maxSum and curLen < minLen):
      maxSum = curSum
      minLen = curLen

F.close()
print( minLen )



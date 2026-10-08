F = open("27-75b.txt")
N = int( F.readline() )
K = 43

tailSum = [0] + [None]*(K-1)
tailLen = [0]*K
maxSum, minLen = 0, 10**10
totalSum = 0

for i in range(N):

  x = int( F.readline() )
  totalSum += x
  r = totalSum % K

  if tailSum[r] != None:
    curSum = totalSum - tailSum[r]
    curLen = i - tailLen[r] + 1
    if curSum > maxSum or \
       (curSum == maxSum and curLen < minLen):
      maxSum = curSum
      minLen = curLen
  else:
    tailSum[r] = totalSum
    tailLen[r] = i+1

F.close()

print( minLen )

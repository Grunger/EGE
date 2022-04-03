def isSpec(x):
  return x % 2 != 0

F = open("27-81b.txt")
N = int(F.readline())

K = 13
tailSum = [0] + [None]*(K-1)
specCount = 0
totalSum = 0
sumMax = 0
for i in range(1,N+1):
  x = int(F.readline())
  totalSum += x
  if isSpec(x):
    specCount += 1
  r = specCount % K
  if tailSum[r] is None:
    tailSum[r] = totalSum
  elif specCount >= K:
    sumMax = max(sumMax, totalSum-tailSum[r])

F.close()

print( specCount, totalSum, tailSum )
print( sumMax )
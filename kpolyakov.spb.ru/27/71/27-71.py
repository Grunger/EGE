with open( "27.txt" ) as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    data.append( int(F.readline()) )

D = 69

tail = [(0,0)] + [(None,0)]*(D-1)
(maxSum, minLen) = (0, 10**10)
total = 0
for i in range(N):
  total += data[i]
  r = total % D
  if tail[r][0] != None:
    curSum = total - tail[r][0]
    curLen = i - tail[r][1] + 1
    if curSum > maxSum or \
       (curSum == maxSum and curLen < minLen):
      maxSum = curSum
      minLen = curLen
  else:
    tail[r] = (total, i)

print( maxSum, minLen )

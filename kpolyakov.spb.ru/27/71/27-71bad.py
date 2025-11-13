with open( "27-71a.txt" ) as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    data.append( int(F.readline()) )

D = 69

(maxSum, minLen) = (0, 10**10)
for i in range(N):
  s = 0
  for j in range(i,N):
    s += data[j]
    if s % D == 0:
      if s > maxSum:
        maxSum, minLen = s, j-i+1
        print( data[i:j+1], maxSum, minLen)
      elif s == maxSum:
        minLen = min( minLen, j-i+1 )

print( maxSum, minLen )

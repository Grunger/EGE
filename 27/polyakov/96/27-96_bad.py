with open("27.txt") as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

maxSum = 0
for i in range(N):
   count5 = count7 = s = 0
   for j in range(i,N):
      s += data[j]
      if data[j] % 5 == 0: count5 += 1
      if data[j] % 7 == 0: count7 += 1
      if count5 == count7:
         if s > maxSum:
           print( s, data[i:j+1] )
         maxSum = max( maxSum, s )

print( maxSum )

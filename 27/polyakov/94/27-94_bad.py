with open("27-94a.txt") as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

maxLen = 0
for i in range(N):
   count5 = count7 = 0
   for j in range(i,N):
     if data[j] % 5 == 0: count5 += 1
     if data[j] % 7 == 0: count7 += 1
     if count5 == count7:
        maxLen = max(maxLen, j-i+1)

print( maxLen )

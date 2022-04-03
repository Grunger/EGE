with open("27-94b.txt") as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

tailLenByDiff = { 0: -1 }

maxLen = 0
count5 = count7 = 0
for i in range(N):
  if data[i] % 5 == 0: count5 += 1
  if data[i] % 7 == 0: count7 += 1
  if count5-count7 not in tailLenByDiff:
    tailLenByDiff[count5-count7] = i
  maxLen = max( maxLen, i - tailLenByDiff[count5-count7] )

print( maxLen )

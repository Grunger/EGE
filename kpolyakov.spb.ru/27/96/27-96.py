with open("27-96a.txt") as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

tailMinSum = { 0: 0 }
totalSum = count5 = count7 = 0
maxSum = None
for i in range(N):
  totalSum += data[i]
  if data[i] % 5 == 0: count5 += 1
  if data[i] % 7 == 0: count7 += 1
  if count5-count7 not in tailMinSum:
    tailMinSum[count5-count7] = totalSum
  else:
    minTail = tailMinSum[count5-count7]
    if maxSum == None or totalSum - minTail > maxSum:
      maxSum = totalSum - minTail
    if totalSum < tailMinSum[count5-count7]:
      tailMinSum[count5-count7] = totalSum

print( maxSum )
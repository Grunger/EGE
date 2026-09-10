def isSpec(x):
  return x % 2 != 0

K = 13
with open("27-81b.txt") as F:
  N = int(F.readline())
  data = []
  cumSum = [0]*N
  for i in range(N):
    x = int(F.readline())
    data.append( x )
    cumSum[i] = x
    if i > 0:
      cumSum[i] += cumSum[i-1]

sMax = 0
for i in range(N):
  if cumSum[-1]-cumSum[i]+data[i] < sMax:
    break
  s = data[i]
  specCount = 1 if isSpec(data[i]) else 0
  for j in range(i+1,N):
    s += data[j]
    if isSpec(data[j]):
      specCount += 1
    if s > sMax and specCount % K == 0:
      sMax = s

print( sMax )

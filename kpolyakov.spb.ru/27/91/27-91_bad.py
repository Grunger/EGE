def isSpecNumber( x ):
  x0 = x
  x = -x
  if x <= 0: return False
  s = 0
  while x:
    s += x % 3
    x //= 3
  return s == 12

f = open('27-91a.txt')
#f = open('27.txt')
n, K, D = map(int, f.readline().split())
data = [ int(f.readline()) for i in range(n) ]
f.close()

maxSum = -10**20
for i in range(n):
  s = 0
  count, countSpec = 0, 0
  for j in range(i, n):
    s += data[j]
    count += 1
    if isSpecNumber(data[j]):
      countSpec += 1
    if countSpec % K == 0 and count % D == 0 and s > maxSum:
      maxSum = s
  # print( data[i], maxSum )

print( maxSum )

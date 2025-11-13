B = 10

F = open("27-47b.txt")

N = int(F.readline())

dMin = [1e6]*B
maxS = 0
minS = 0
for i in range(N):
  a, b = map( int, F.readline().split() )
  # print( *sorted([a, b]) )
  maxS += max(a, b)
  minS += min(a, b)
  d = abs(a - b)
  r = d % B
  dMinNew = dMin[:]
  if r > 0:
    for k in range(1, B):
      r0 = (r + k) % B
      dMinNew[r0] = min( d + dMin[k], dMinNew[r0] )
  dMinNew[r] = min( d, dMinNew[r] )
  dMin = dMinNew[:]

print( maxS, minS )
print( dMin )
D = maxS % B
if minS % B == D:
  ans = minS
else:
  r0 = D - minS % B
  if r0 < 0: r0 += B
  ans = minS + dMin[r0]

print( "Ответ:", ans )

F.close()
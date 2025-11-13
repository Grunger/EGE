B = 7

F = open("27-46b.txt")

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

print( maxS, maxS % B )
print( minS, minS % B )
print( dMin )
D = minS % B
if maxS % B == D:
  ans = maxS
else:
  r0 = maxS % B - D
  if r0 < 0: r0 += B
  ans = maxS - dMin[r0]

print( "Ответ:", ans )
print( minS % B, ans % B )

F.close()
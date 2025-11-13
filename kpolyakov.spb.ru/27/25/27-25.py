Fin = open("27-25b.txt")

N = int( Fin.readline() )
B = 8
D = 3

dMin = [100001]*B
s = 0
for i in range(N):
  a, b = map( int, Fin.readline().split() )
  s += max( a, b )
  d = abs( a-b )
  r = d % B
  dMinNew = dMin[:]
  for k in range(1, B):
    r0 = (r + k) % B
    dMinNew[r0] = min( d+dMin[k], dMinNew[r0] )
  dMinNew[r] = min( d, dMinNew[r] )
  dMin = dMinNew[:]

if s % B == D:
  print( s, s % B )
else:
  print( s, s % B, dMin )
  r0 = s % B - D
  if r0 < 0: r0 += B
  s -= dMin[r0]
  print( s, oct(s) )

Fin.close()
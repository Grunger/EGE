Fin = open("27-26a.txt")

N = int( Fin.readline() )
B = 16
D = 15

dMin = [100001]*B
s = 0
for i in range(N):
  a, b = map( int, Fin.readline().split() )
  s += min( a, b )
  d = abs( a-b )
  r = d % B
  dMinNew = dMin[:]
  for k in range(1, B):
    r0 = (r + k) % B
    dMinNew[r0] = min( d+dMin[k], dMinNew[r0] )
  dMinNew[r] = min( d, dMinNew[r] )
  dMin = dMinNew[:]

if s % B == D:
  print( s, hex(s) )
else:
  print( s, s % B, dMin )
  r0 = D - s % B
  if r0 < 0: r0 += B
  s += dMin[r0]
  print( s, hex(s) )

Fin.close()
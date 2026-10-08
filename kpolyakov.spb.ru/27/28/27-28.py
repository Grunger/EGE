Fin = open("27-28b.txt")

N = int( Fin.readline() )
B = 8
D = 2

dMin = 100001
s = 0
for i in range(N):
  a, b = map( int, Fin.readline().split() )
  s += min( a, b )
  d = abs( a-b )
  r = d % B
  if r != 0:
    dMin = min( d, dMin )

if s % B != D:
  print( s, oct(s) )
else:
  print( s, s % B, dMin )
  s += dMin
  print( s, oct(s) )

Fin.close()
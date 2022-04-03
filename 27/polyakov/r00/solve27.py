Fin = open("27.txt")

N = int( Fin.readline() )

s, dMin  = 0, 10001
for i in range(N):
  a, b = map( int, Fin.readline().split() )
  s += max( a, b )
  d = abs( a-b )
  if d % 3 > 0:
    dMin = min( d, dMin )

if s % 3 != 0:
  print( s )
else:
  print( s-dMin )

Fin.close()
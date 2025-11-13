Fin = open("27-1a.txt")

N = int( Fin.readline() )

D = 3

s, dMin  = 0, 10001
for i in range(N):
  a, b = map( int, Fin.readline().split() )
  s += min( a, b )
  d = abs( a-b )
  if d % D > 0:
    dMin = min( d, dMin )

if s % D != 0:
  print( s )
else:
  print( s, s%D, dMin )
  print( s+dMin )

Fin.close()
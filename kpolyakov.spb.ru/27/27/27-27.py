Fin = open("27-27a.txt")

N = int( Fin.readline() )
B = 16
D = 10

dMin = 100001
s = 0
for i in range(N):
  a, b = map( int, Fin.readline().split() )
  s += max( a, b )
  d = abs( a-b )
  r = d % B
  if r != 0:
    dMin = min( d, dMin )

if s % B != D:
  print( s, hex(s) )
else:
  print( s, s % B, dMin )
  s -= dMin
  print( s, hex(s) )

Fin.close()
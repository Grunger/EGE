Fin = open("27-32b.txt")

D = 11

N = int( Fin.readline() )

s, dMin  = 0, [10001]*D
for i in range(N):
  abc = sorted( list( map( int, Fin.readline().split() ) ) )
  s += abc[0]
  dMinNew = dMin[:]
  for x in abc[1:]:
    d = x - abc[0]
    r = d % D
    if r > 0:
      for k in range(1, D):
        r0 = (r + k) % D
        dMinNew[r0] = min( d+dMin[k], dMinNew[r0] )
      dMinNew[r] = min( d, dMinNew[r] )
  dMin = dMinNew[:]

if s % D == 0:
  print( s, s % D )
else:
  print( s, s % D )
  print( dMin )
  s += dMin[D - s % D]
  print( s, s % D  )

Fin.close()

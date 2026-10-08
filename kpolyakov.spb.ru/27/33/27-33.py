Fin = open("27.txt")

D = 4

N = int( Fin.readline() )

s, dMin  = 0, [10001]*D
for i in range(N):
  abc = list( map( int, Fin.readline().split() ) )
  a, b, c = abc
  abc = sorted( [abc[0]+abc[1], abc[0]+abc[2], abc[1]+abc[2]], reverse=True )
  s += abc[0]
  dMinNew = dMin[:]
  for x in abc[1:]:
    d = abc[0] - x
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
  print( "Коррекция" )
  print( dMin )
  s -= dMin[s % D]
  print( s, s % D  )

Fin.close()
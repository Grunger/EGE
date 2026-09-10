Fin = open("27-29b.txt")

N = int( Fin.readline() )
D = 5

mind, s = 20004, 0
for i in range(N):
  abc = [int(x) for x in Fin.readline().split()]
  abc = [abc[0]+abc[1], abc[0]+abc[2], abc[1]+abc[2]]
  m = max(abc)
  s += m
  for x in abc:
    if (m - x) % D != 0 and m-x < mind:
      mind = m - x

if s % D == 0:
  s -= mind

if s % D != 0:
  print( s )
else:
  print( 0 )

Fin.close()
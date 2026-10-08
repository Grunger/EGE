Fin = open("27.txt")

N = int( Fin.readline() )
D = 9

mind, s = 20004, 0

for i in range(N):
  abc = [int(x) for x in Fin.readline().split()]
  abc = [abc[0]+abc[1], abc[0]+abc[2], abc[1]+abc[2]]
  m = min(abc)
  s += m
  for x in abc:
    if (x - m) % D != 0 and x - m < mind:
      mind = x - m
      print( abc, x - m )
  print(i, s, mind)

print(s, mind)

if s % D == 0:
  s += mind

if s % D != 0:
  print( s )
else:
  print( 0 )

Fin.close()
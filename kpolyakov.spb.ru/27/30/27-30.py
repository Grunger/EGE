Fin = open("27-30b.txt")

N = int( Fin.readline() )
D = 7

mind, s = 20004, 0
for i in range(N):
  abc = [int(x) for x in Fin.readline().split()]
  m = min(abc)
  s += m
  for x in abc:
    if (x - m) % D != 0 and x - m < mind:
      mind = x - m
      # print( abc, m-x )

print(s, mind)

if s % D == 0:
  s += mind

if s % D != 0:
  print( s )
else:
  print( 0 )

Fin.close()
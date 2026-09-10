# На основе решения А. Кабанова

def Nod( a, b ):
  if a*b == 0: return a+b
  else: return Nod( b, a%b )

Fin = open("27-36b.txt")

N = int( Fin.readline() )

B = 10
D = 0

sums = [0 for i in range(B)]
for i in range(N):
  a,b,c = list(map( int, Fin.readline().split() ))
  abc = [Nod(a,b), Nod(a,c), Nod(b,c)]
  sumsNext = [0]*B
  for s in sums:
    for x in abc:
      r = s + x
      if (i == 0 or s != 0) and  r > sumsNext[r%B]:
        sumsNext[r%B] = r
  sums = sumsNext[:]

Fin.close()

print( sums[D] )

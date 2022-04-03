# На основе решения А. Кабанова

Fin = open("27-34b.txt")

N = int( Fin.readline() )

B = 6
D = 0

INF = 10**10
sums = [0 for i in range(B)]
for i in range(N):
  a,b,c = list(map( int, Fin.readline().split() ))
  abc = [a+b, a+c, b+c]
  sumsNext = [INF]*B
  for s in sums:
    for x in abc:
      r = s + x
      if r < sumsNext[r%B]:
        sumsNext[r%B] = r
  sums = sumsNext[:]

Fin.close()

print( sums[D] )

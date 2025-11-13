# На основе решения А. Кабанова

Fin = open("27-47b.txt")

N = int( Fin.readline() )

B = 10

totalMax = 0
INF = 10**10
sums = [0 for i in range(B)]
for i in range(N):
  abc = list(map( int, Fin.readline().split() ))
  totalMax += max(abc)
  sumsNext = [INF]*B
  for s in sums:
    for x in abc:
      r = s + x
      if r < sumsNext[r%B]:
        sumsNext[r%B] = r
  sums = sumsNext[:]

Fin.close()

D = totalMax % B
print( sums[D] )

# На основе решения А. Кабанова

Fin = open("27-41b.txt")

N = int( Fin.readline() )

B = 7
D = 0

total = 0
INF = 10**10
sums = [0 for i in range(B)]
for i in range(N):
  abc = list(map( int, Fin.readline().split() ))
  total += sum(abc)
  sumsNext = [INF]*B
  for s in sums:
    for x in abc:
      r = s + x
      if r < sumsNext[r%B]:
        sumsNext[r%B] = r
  sums = sumsNext[:]

Fin.close()

print( min([s for s in sums
              if (total-s) % 2 == 1 ]) )

# На основе решения А. Кабанова

Fin = open("27-40b.txt")

N = int( Fin.readline() )

B = 2
D = 0

total = 0
sums = [0 for i in range(B)]
for i in range(N):
  abc = list(map( int, Fin.readline().split() ))
  total += sum(abc)
  sumsNext = [0]*B
  for s in sums:
    for x in abc:
      r = s + x
      if (i == 0 or s != 0) and  r > sumsNext[r%B]:
        sumsNext[r%B] = r
  sums = sumsNext[:]

Fin.close()

print( max([s for s in sums
              if (total-s) % 2 == 1 ]) )

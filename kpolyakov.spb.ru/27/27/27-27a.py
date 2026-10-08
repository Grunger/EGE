# На основе решения А. Кабанова

Fin = open("27-27b.txt")

N = int( Fin.readline() )

B = 16
D = 10

sums = [0 for i in range(B)]
for i in range(N):
  ab = list(map( int, Fin.readline().split() ))
  sumsNext = [0]*B
  for s in sums:
    for x in ab:
      r = s + x
      if (i == 0 or s != 0) and  r > sumsNext[r%B]:
        sumsNext[r%B] = r
  sums = sumsNext[:]

Fin.close()

del sums[D]
print( max(sums) )

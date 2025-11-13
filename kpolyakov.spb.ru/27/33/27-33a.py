# На основе решения А. Кабанова

Fin = open("27.txt")

N = int( Fin.readline() )

B = 4
D = 0

sums = [0 for i in range(B)]
for i in range(N):
  a,b,c = list(map( int, Fin.readline().split() ))
  abc = [a+b, a+c, b+c]
  sumsNext = [0]*B
  for s in sums:
    for x in abc:
      r = s + x
      if (i == 0 or s != 0) and  r > sumsNext[r%B]:
        sumsNext[r%B] = r
  sums = sumsNext[:]

Fin.close()

print( sums[D] )

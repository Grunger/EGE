Fin = open("27-14b.txt")

N = int( Fin.readline() )
D = 12

count = 0
remCount = [0]*D
for i in range(N):
  x = int( Fin.readline() )
  r = x % D
  count += remCount[(D - r) % D]
  remCount[r] += 1

print( count )

Fin.close()
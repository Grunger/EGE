Fin = open("27-7b.txt")

N = int( Fin.readline() )

max7 = 0
maxX = 0
for i in range(N):
  x = int( Fin.readline() )
  if x > max7 and x % 7 == 0 and x % 49 != 0:
    max7 = x
  if x % 7 != 0  and  x > maxX:
    maxX = x

R = max7*maxX
if R == 0: R = 1

print( max7, maxX )
print( R )

Fin.close()
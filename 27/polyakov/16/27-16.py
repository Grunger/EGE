Fin = open("27-16b.txt")

N = int( Fin.readline() )

count = 0
k26 = k13 = k2 = k1 = 0
for i in range(N):
  x = int( Fin.readline() )
  if x % 13 == 0:
    if x % 2 == 0:
      count += k1
      k26 += 1
      k2 += 1
    else:
      count += k2
      k13 += 1
      k1 += 1
  elif x % 2 == 0:
    count += k13
    k2 += 1
  else:
    count += k26
    k1 += 1

print( count )

Fin.close()
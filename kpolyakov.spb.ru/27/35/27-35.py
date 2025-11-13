Fin = open("27-35b.txt")

N = int( Fin.readline() )

count = 0
countOdd = 0
countEven = 0
countOddFrom0 = 0
countEvenFrom0 = 0
for i in range(N):
  x = int(Fin.readline())
  if x == 0:
    countEvenFrom0 = countOddFrom0 = 0
  elif x % 2 == 0:
    count += countEven - countEvenFrom0
    countEven += 1
    countEvenFrom0 += 1
  else:
    count += countOdd - countOddFrom0
    countOdd += 1
    countOddFrom0 += 1

print(count)

Fin.close()

Fin = open("27-12b.txt")

N = int( Fin.readline() )

count = 0
m2 = m3 = m6 = 0
for i in range(N) :
  x = int( Fin.readline() )
  if x % 6 == 0:
    count += i
    m6 += 1
  else:
    if x % 2 == 0:
      count += m3 + m6
      m2 += 1
    elif x % 3 == 0:
      count += m2 + m6
      m3 += 1
    else:
      count += m6

print( count )

Fin.close()
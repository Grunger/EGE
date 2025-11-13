Fin = open("27-18b.txt")

N = int( Fin.readline() )

def handle( x ):
  global count, k26, k13, k2, k1
  if x % 13 == 0:
    if x % 2 == 0:
      count += k1
      k26, k2 = k26+1, k2+1
    else:
      count += k2
      k13, k1 = k13+1, k1+1
  elif x % 2 == 0:
    count += k13
    k2 += 1
  else:
    count += k26
    k1 += 1

L = 5
queue = []
count = k26 = k13 = k2 = k1 = 0
for i in range(L):
  x = int( Fin.readline() )
  queue.append(x)
  handle( x )
  print( x, x % 2, x % count, k26, k13, k2, k1 )

print( queue )

for i in range( L, N ):
  # элемент удаляется из очереди
  a = queue.pop(0)
  if a % 13 == 0:
    if a % 2 == 0:
      k26, k2 = k26-1, k2-1
    else:
      k13, k1 = k13-1, k1-1
  elif a % 2 == 0:
    k2 -= 1
  else:
    k1 -= 1
  # вводим элемент
  x = int( Fin.readline() )
  queue.append( x )
  handle( x )
  #print( x, count, k26, k13, k2, k1 )

print( count )

Fin.close()
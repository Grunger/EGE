Fin = open("27-17b.txt")

N = int( Fin.readline() )

L = 5
queue = []
for i in range(L):
  queue.append( int(Fin.readline()) )

count = 0
k26 = k13 = k2 = k1 = 0
for i in range(N-L):
    # элемент из очереди
  a = queue.pop(0)
  if a % 13 == 0:
    if a % 2 == 0:
      k26, k2 = k26+1, k2+1
    else:
      k13, k1 = k13+1, k1+1
  elif a % 2 == 0:
    k2 += 1
  else:
    k1 += 1
    # вводим элемент
  x = int( Fin.readline() )
  queue.append( x )
  if x % 13 == 0:
    if x % 2 == 0:
      count += k1
    else:
      count += k2
  elif x % 2 == 0:
    count += k13
  else:
    count += k26

print( count )

Fin.close()
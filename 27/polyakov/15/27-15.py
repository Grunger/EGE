Fin = open("27-15a.txt")

N = int( Fin.readline() )
D = 14
L = 5
queue = []
for i in range(L):
  queue.append( int(Fin.readline()) )

count = 0
remCount = [0]*D
for i in range(N-L):
  a = queue.pop(0)
  remCount[a % D] += 1
  x = int( Fin.readline() )
  queue.append( x )
  r = x % D
  count += remCount[(D - r) % D]

print( count )

Fin.close()
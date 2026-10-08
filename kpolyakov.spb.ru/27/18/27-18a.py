Fin = open("27-18b.txt")

N = int( Fin.readline() )

data = []
for line in Fin:
  if line.strip():
    data.append( int(line) )

Fin.close()

L = 5
count = 0
for i in range(N-1):
  for j in range(i+1, min(i+L,N)):
    if (data[i]+data[j]) % 2 != 0 and (data[i]*data[j]) % 13 == 0:
      count += 1

print( count )


F = open( "27.txt" )

N = int(F.readline())
data = []
for i in range(N):
  data.append( int(F.readline()) )

mi = 10**10
for i in range(N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      s = data[i] + data[j] + data[k]
      if s % 3 == 0:
        print( data[i], data[j], data[k], s )
        if s < mi: mi = s

print( mi )




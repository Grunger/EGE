F = open( "27.txt" )

N = int(F.readline())
data = []
for i in range(N):
  data.append( int(F.readline()) )

ma = -10**10
for i in range(N-3):
  for j in range(i+1,N-2):
    for k in range(j+1,N-1):
      for m in range(k+1,N):
        s = data[i] + data[j] + data[k] + data[m]
        if s % 4 == 0:
          print( (data[i], data[j], data[k], data[m]), s )
          if s > ma: ma = s

print( ma )




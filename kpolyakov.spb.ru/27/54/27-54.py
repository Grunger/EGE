F = open( "27-54b.txt" )

N = int(F.readline())
data = []
for i in range(N):
  data.append( int(F.readline()) )

ma1 = [-10**10]*4
ma2 = [-10**10]*4
ma3 = [-10**10]*4

ma = -10**10
for i in range(N):
  d = data[i] % 4
  ma = max(ma, data[i]+ma3[(4-d)%4])
  ma3new = ma3
  for k in range(4):
    d0 = (k + d) % 4
    ma3new[d0] = max( ma3[d0], ma2[k]+data[i] )
  ma3 = ma3new
  ma2new = ma2
  for k in range(4):
    d0 = (k + d) % 4
    ma2new[d0] = max( ma2[d0], ma1[k]+data[i] )
  ma2 = ma2new
  ma1[d] = max(ma1[d], data[i])
  #print( data[i], ma1, ma2, ma3, ma )

print( ma )


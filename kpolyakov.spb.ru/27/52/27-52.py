F = open( "27-52a.txt" )

N = int(F.readline())
data = []
for i in range(N):
  data.append( int(F.readline()) )

ma1 = [-10**10]*3
ma2 = [-10**10]*3

ma = -10**10
for i in range(N):
  d = data[i] % 3
  ma = max(ma, data[i]+ma2[(3-d)%3])
  ma2new = ma2
  for k in range(3):
    d0 = (k + d) % 3
    ma2new[d0] = max( ma2[d0], ma1[k]+data[i] )
  ma2 = ma2new
  ma1[d] = max(ma1[d], data[i])
  #print( data[i], ma1, ma2, ma )

print( ma )




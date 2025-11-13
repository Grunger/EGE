F = open( "27-55b.txt" )

N = int(F.readline())
data = []
for i in range(N):
  data.append( int(F.readline()) )

mi1 = [10**10]*4
mi2 = [10**10]*4
mi3 = [10**10]*4

mi = 10**10
for i in range(N):
  d = data[i] % 4
  mi = min(mi, data[i]+mi3[(4-d)%4])
  mi3new = mi3
  for k in range(4):
    d0 = (k + d) % 4
    mi3new[d0] = min( mi3[d0], mi2[k]+data[i] )
  mi3 = mi3new
  mi2new = mi2
  for k in range(4):
    d0 = (k + d) % 4
    mi2new[d0] = min( mi2[d0], mi1[k]+data[i] )
  mi2 = mi2new
  mi1[d] = min(mi1[d], data[i])
  #print( data[i], mi1, mi2, mi )

print( mi )




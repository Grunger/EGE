F = open( "27-53b.txt" )

N = int(F.readline())
data = []
for i in range(N):
  data.append( int(F.readline()) )

mi1 = [10**10]*3
mi2 = [10**10]*3

mi = 10**10
for i in range(N):
  d = data[i] % 3
  mi = min(mi, data[i]+mi2[(3-d)%3])
  mi2new = mi2
  for k in range(3):
    d0 = (k + d) % 3
    mi2new[d0] = min( mi2[d0], mi1[k]+data[i] )
  mi2 = mi2new
  mi1[d] = min(mi1[d], data[i])
  #print( data[i], mi1, mi2, mi )

print( mi )




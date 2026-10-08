F = open( "27-57b.txt" )

N = int(F.readline())
data = []
for i in range(N):
  data.append( int(F.readline()) )

D = 9

mi1 = [10**10]*D
mi2 = [10**10]*D
mi3 = [10**10]*D

mi = 10**10
for i in range(N):
  d = data[i] % D
  mi = min(mi, data[i]+mi3[(D-d)%D])
  mi3new = mi3
  for k in range(D):
    d0 = (k + d) % D
    mi3new[d0] = min( mi3[d0], mi2[k]+data[i] )
  mi3 = mi3new
  mi2new = mi2
  for k in range(D):
    d0 = (k + d) % D
    mi2new[d0] = min( mi2[d0], mi1[k]+data[i] )
  mi2 = mi2new
  mi1[d] = min(mi1[d], data[i])
  #print( data[i], mi1, mi2, mi )

print( mi )




Fin = open("27-19b.txt")

N = int( Fin.readline() )

x = int( Fin.readline() )
dp_min = dp_max = ma = x
for i in range(N-1):
  x = int( Fin.readline() )
  t = min( dp_min*x, min(dp_max*x, x) )
  dp_max = max(dp_min*x, max(dp_max*x, x))
  dp_min = t
  ma = max(ma, dp_max)
  # print(x, ma)

print( ma )

Fin.close()
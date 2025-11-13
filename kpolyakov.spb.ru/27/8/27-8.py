Fin = open("27-8b.txt")

N = int( Fin.readline() )

K = 5
Buf = [0]*K
minPrev = 1001
R = 2*1000**2 + 1
for i in range(N):
  if i >= K:
    minPrev = min(minPrev, Buf[i % K])
  Buf[i % K] = int( Fin.readline() )
  R = min(R, minPrev**2 + Buf[i % K]**2)

print(R)

Fin.close()
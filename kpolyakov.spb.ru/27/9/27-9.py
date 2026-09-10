Fin = open("27-9b.txt")

N = int( Fin.readline() )

K = 6
Buf = [0]*K
minOdd = 1000
minRes = 1000000
for i in range(N):
  if i >= K:
    if Buf[i % K] % 2 == 1:
      minOdd = min(minOdd, Buf[i % K])
  Buf[i % K] = int( Fin.readline() )
  if minOdd != 1000 and Buf[i % K] % 2 == 1:
    minRes = min(minRes, minOdd*Buf[i % K])

if minRes == 1000000:
  print(-1)
else:
  print(minRes)

Fin.close()
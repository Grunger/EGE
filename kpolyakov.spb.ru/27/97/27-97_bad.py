#with open('27.txt') as F:
with open('27-97a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for i in range(N) ]

count = 0
for i, x in enumerate(data):
  s = 0
  for j in range(i, N):
    s += data[j]
    if s % K == 0:
      count += 1
      #print( data[i:j+1] )

print( count )
F = open('27-79b.txt')
N = int(F.readline())

startX = set()
startPos = {}
lenMax = 0
for i in range(1, N+1):
  x = int( F.readline() )
  if x % 21 == 0:
    if not x in startX:
      startX.add( x )
      startPos[x] = i-1
  if x*x in startX:
    lenMax = max( lenMax, i-startPos[x*x] )

F.close()

print( lenMax )

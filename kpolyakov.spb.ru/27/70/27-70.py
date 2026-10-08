F = open( "27-70b.txt" )
N = int(F.readline())

D = 5
maxDiff = 0
diff = [1000]*D
for i in range(N):
  a, b = sorted( map(int, F.readline().split()) )
  maxDiff += b - a
  r = (b - a) % D
  if r:
    dNew = diff[:]
    for k in range(D):
      r0 = (k + 2*r) % D
      dNew[r0] = min( dNew[r0], diff[k]+2*(b-a) )
    r1 = (2*r) % D
    dNew[r1] = min( dNew[r1], 2*(b-a) )
    diff = dNew[:]

print( maxDiff, maxDiff % D )
print( diff )
if maxDiff % D == 0:
  print( maxDiff )
else:
  print( *[maxDiff-x for x in diff
                     if (maxDiff-x) % D == 0 ] )



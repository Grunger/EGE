Fin = open("27-44b.txt")

N = int(Fin.readline())

s1 = s2 = s3 = 0
diff0 = []
diff1 = [ (1e10, -1), (1e10, -1) ]
diff2 = [ (1e10, -1), (1e10, -1) ]

for i in range(N):
  a, b, c = map( int, Fin.readline().split() )
  a, b, c = sorted( [a, b, c] )
  #print( a, b, c, c-a, c-b )
  s1 += a
  s2 += b
  s3 += c
  if (a - b) % 2 == 1:
    diff0.append(i)
  if (c - a) % 2 == 1:
    delta = c - a
    if (c - b) % 2 == 1:
      delta = c-b
    if delta < diff1[0][0]:
      diff1 = [ (delta, i), diff1[0] ]
    elif delta < diff1[1][0]:
      diff1[1] = (delta, i)
  if (c - b) % 2 == 1:
    delta = c - b
    if delta < diff2[0][0]:
      diff2 = [ (delta, i), diff2[0] ]
    elif delta < diff2[1][0]:
      diff2[1] = (delta, i)
  #print( s1, s2, s3, diff1, diff2 )

Fin.close()

print( 's1 =', s1, 's2 =', s2 )
print( 's3 =', s3 )
print( 'b <-> a:', diff0 )
print( 'c <-> a:', diff1 )
print( 'c <-> b:', diff2 )

print("Ответ:")
if s1 % 2 == 1  and  s2 % 2 == 1:
  print( s3 )
elif s1 % 2 == 0 and s2 % 2 == 0:
  if diff0:
    print( s3 )
  else:
    d = min( diff1[0][0] + diff2[1][0],
             diff1[1][0] + diff2[0][0],
             diff1[0][0] + diff1[1][0],
             diff2[0][0] + diff2[1][0] )
    if diff1[0][1] != diff2[0][1]:
      d = min( d,  diff1[0][0] + diff2[0][0] )
    print( s3 - d )
elif s1 % 2 == 0:
  diff = diff1[0][0]
  if diff0:
    if len(diff0) > 1 or diff2[0][1] != diff0[0]:
      diff = min( diff, diff2[0][0] )
    elif diff2[1][1] != diff0[0]:
      diff = min( diff, diff2[1][0] )
  print( s3 - diff )
elif s2 % 2 == 0:
  print( s3 - diff2[0][0] )



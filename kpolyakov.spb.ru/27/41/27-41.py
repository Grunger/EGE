Fin = open("27-41b.txt")

N = int(Fin.readline())
s1 = s2 = s3 = 0
diff = 1e10
for i in range(N):
  a, b, c = map( int, Fin.readline().split() )
  a, b, c = sorted( [a, b, c] )[::-1]
  s1 += a
  s2 += b
  s3 += c
  if (a - c) % 2 == 1:
    diff = min(diff, a-c)
  if (b - c) % 2 == 1:
    diff = min(diff, b-c)

Fin.close()

if s1 % 2 != s2 % 2:
  print( s3 )
else:
  print( s3 + diff )


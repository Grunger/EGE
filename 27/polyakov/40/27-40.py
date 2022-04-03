Fin = open("27-40b.txt")

N = int(Fin.readline())
s1 = s2 = s3 = 0
diff = 1e10
for i in range(N):
  a, b, c = map( int, Fin.readline().split() )
  a, b, c = sorted( [a, b, c] )
  s1 += a
  s2 += b
  s3 += c
  if (c - a) % 2 == 1:
    diff = min(diff, c-a)
  if (c - b) % 2 == 1:
    diff = min(diff, c-b)

Fin.close()

if s1 % 2 != s2 % 2:
  print( s3 )
else:
  print( s3 - diff )


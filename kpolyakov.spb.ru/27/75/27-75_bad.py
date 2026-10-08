k = 43
with open('27-75a.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    data.append( int(F.readline()) )

sMax, minLen = 0, 10**10
for start in range(N):
  s = 0
  for last in range(start,N):
    s += data[last]
    if s % k == 0 and \
       (s > sMax or (s == sMax and last-start < minLen)):
      sMax = s
      minLen = last - start

print( minLen + 1 )

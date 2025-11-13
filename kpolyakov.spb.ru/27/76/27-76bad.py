with open('27-76a.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    data.append( int(F.readline()) )

count = 0
for i in range(N-1):
  for j in range(i+2,N):
    s = sum(data[i+1:j])
    if (data[i]+data[j]) % 3 == 0 and s % 2 == 0:
      # print( data[i], data[j], data[i]+data[j], s )
      count += 1

print( count )
def isSpecNumber(x):
  return x < 0 and abs(x) % 10 == 3

f = open('27-93a.txt')
N, K = map( int, f.readline().split() )
data = [int(f.readline()) for x in range(N)]
f.close()

maxSum = -10**20
maxSumData = 0, 0
for i in range(N):
  s, count = 0, 0
  for j in range(i,N):
    s += data[j]
    if isSpecNumber(data[j]):
       count += 1
    if count == K:
      if s > maxSum:
        maxSum = s
        maxSumData = i, j
  # print(f"{x:2}, {sumTotal:2},  {maxSum:2}, {minTails}")


print( maxSum, maxSumData )

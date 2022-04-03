with open('27-84b.txt') as f:
    n, k = map(int, f.readline().split())
    nums = [int(f.readline()) for i in range(n)]

sumCount = {0: 0}
for x in nums:
  newCount = {}
  for s0 in sumCount:
    newSum = s0 + x
    if newSum < 2*k and \
       (newSum not in sumCount or
        sumCount[s0]+1 > sumCount[newSum]):
       newCount[newSum] = sumCount[s0] + 1
  sumCount |= newCount

res = [(key,sumCount[key]) for key in sumCount]
res.sort( key = lambda x: (abs(x[0]-k), -x[1]))

print( res[0] )

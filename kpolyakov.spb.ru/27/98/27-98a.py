
with open('27-98b.txt') as F:
  N, K = [ int(x) for x in F.readline().split() ]
  data = [ int(F.readline()) for i in range(N) ]

minLen = 10**10
last = [-1]*(K+1)
for i in range(N):
  last[data[i]] = i
  if last.count(-1) == 1:
    minLen = min( minLen, i-min(last[1:])+1 )

print( minLen )




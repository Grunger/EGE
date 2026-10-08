MAXDELTA = 100

with open("27-62.txt") as F:
  n = int(F.readline())
  data = []
  next = []
  for i in range(n):
    data.append(int(F.readline()))
    next.append([0]*(MAXDELTA+1))

data.sort()
for i in range(n):
  k = i + 1
  while k < n and data[k]-data[i] <= MAXDELTA:
    d = data[k] - data[i]
    next[i][d] = k
    k += 1

maxLen = (0, 1)
for d in range(1,MAXDELTA+1):
  path = [x[d] for x in next]
  mLen = 1
  for start in range(len(path)-mLen):
    if path[start] > 0:
      curLen = 1
      i = start
      while i < len(path) and path[i] > 0:
        curLen += 1
        mLen = max(mLen, curLen)
        i = path[i]
  if mLen > maxLen[1]:
    maxLen = (d, mLen)

print( maxLen )

with open("27-95b.txt") as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

count = 0
tailDiffCount = { 0: 1 }
count5 = count7 = 0
for i in range(N):
  if data[i] % 5 == 0: count5 += 1
  if data[i] % 7 == 0: count7 += 1
  if count5-count7 not in tailDiffCount:
    tailDiffCount[count5-count7] = 0
  count += tailDiffCount[count5-count7]
  tailDiffCount[count5-count7] += 1
  # print( data[i], count, tailDiffCount )

print( count )
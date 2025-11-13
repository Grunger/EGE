# Автор: А. Кабанов

def isSpecNumber(x):
  return x < 0 and abs(x) % 10 == 7

f = open('27-86b.txt')
n, K = map(int, f.readline().split())

maxSum = -10**20
minTails = [10**20]*K

sumTotal = 0
count = 0
for i in range(n):
  x = int(f.readline())
  sumTotal += x

  if isSpecNumber(x):
    count += 1

  r = count % K
  if r == 0 and sumTotal > maxSum:
    maxSum = sumTotal

  if minTails[r] != 10**20 and sumTotal - minTails[r] > maxSum:
    maxSum = sumTotal - minTails[r]

  minTails[r] = min( minTails[r], sumTotal )

f.close()

print( maxSum )

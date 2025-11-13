def reversedNum(x):
  return int(str(x)[::-1])

def sumDigits(n):
  return sum(map(int, str(n)))

Fin = open("27-39b.txt")

revX =  [reversedNum(x) for x in range(1000)]

symmCount = [0]*1000
count = [0]*1000

N = int(Fin.readline())
for i in range(N):
  x = int(Fin.readline())
  if x == revX[x]:
    symmCount[x] += 1   # подсчёт симметричных чисел
  else:
    count[x] += 1       # подсчёт несимметричных чисел

verbose = 0

if verbose:
  d = {}
  d1 = {}
  for x in range(1000):
     if symmCount[x] > 0:
        d[x] = symmCount[x]
     if count[x] > 0: d1[x] = count[x]
  print(d)
  print(d1)

maxCenter = 0
for x in range(1000):
  if symmCount[x] % 2 == 1:
    #if sumDigits(x) > sumDigits(maxCenter):
      maxCenter = x
  if symmCount[x] != 0:
    count[x] = symmCount[x] // 2

if verbose:
  print(maxCenter)

  d1 = {}
  for x in range(1000):
     if count[x] > 0: d1[x] = count[x]
  print(d1)

ans = sumDigits(maxCenter)
symmNumber = str(maxCenter)
for x in range(1000):
  if x <= revX[x]:   # чтобы не учитывать пару повторно
    ans += 2 * sumDigits(x) * min(count[x], count[revX[x]])
    if count[x]*count[revX[x]]:
      symmNumber = str(revX[x]) + symmNumber + str(x)

if verbose:
  print(symmNumber)

print(ans)

Fin.close()

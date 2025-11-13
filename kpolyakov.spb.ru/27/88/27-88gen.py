from random import randint, choice

def getAllPrimes(N):
  res = list(range(N+1))
  res[1] = 0
  x = 2
  while x*x <= N:
    if x:
       for k in range(2*x, N+1, x):
          res[k] = 0
    x += 1
  return [x for x in res if x != 0]

MAX = 1000000
primes = getAllPrimes( MAX )

fileName = '27-88a.txt'
N = 150000
N = 280
K = 13

with open(fileName, 'w') as f:
   print( N, K, file = f )
   for i in range(N):
      if randint(0, 1) == 0:
        print( randint(-MAX, MAX),  file = f )
      else:
        prime = choice( primes )
        if randint(0, 1) == 0:
          print( prime,  file = f )
        else:
          print( -prime,  file = f )

s = 0
with open(fileName) as f:
  N, K = map(int, f.readline().split())
  for i in range(N):
    x = int(f.readline())
    s = max( x, s+x )

print(s)



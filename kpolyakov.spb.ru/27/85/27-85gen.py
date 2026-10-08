from random import randint

N = 150000
K = 111

with open('27-85b.txt', 'w') as f:
   print( N, K, file = f )
   for i in range(N):
      print( randint(-1000, 1000),  file = f )
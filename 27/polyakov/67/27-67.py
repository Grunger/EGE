D = 5
with open('27-67.txt') as Fin:
  N = int(Fin.readline())
  diffEven, diffOdd, diffPair = [10**10]*3
  S = 0
  for i in range(min(N,100000)):
    data = list(map(int, Fin.readline().split()))[1:]

    even = sorted( [x for x in data if x % 2 == 0] )
    odd = sorted( [x for x in data if x % 2 != 0] )
    if len(even) > 1 or len(odd) > 1:
      for e in even:
        if e % D != 0: # удалёем одно чётное
          diffEven = min(diffEven, e)
          break

    if len(odd) % 2 != 0:
      minOdd = odd[0]
      del odd[0]
      for o in odd:
        if (o - minOdd) % D != 0: # меняем нечётное <-> нечётное
          diffOdd = min(diffOdd, o-minOdd)
          break

    nOdd = len(odd)
    if nOdd > 2 or len(even) > 0:
      for i1 in range(nOdd):
        for i2 in range(i1+1,nOdd):
          if (odd[i1] + odd[i2]) % D != 0: # удаляем пару нечётных
            diffPair = min(diffPair, odd[i1] + odd[i2])

    S += sum(even) + sum(odd)

print( S, diffEven, diffOdd, diffPair )
if S % D == 0:
  S -= min( diffEven, diffOdd, diffPair )
print( S )

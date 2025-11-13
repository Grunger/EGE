# Неверно работает, если искомая подпоследовательность
# вообще не содержит особых чисел

with open('27-85b.txt') as f:
  N, K = map( int, f.readline().split() )
  data = [ int(f.readline()) for i in range(N) ]

def isSpecNumber(x):
  return x > 0 and x % 2 == 0

sumSpec = []   # суммы от начала о каждого особого числа
tailSpec = []  # хвосты с наибольшей суммой

countSpec = 0  # количество найденных особых чисел

sumTotal = 0   # накапливаемая сумма от начала до текущего числа

sumBetween = 0     # сумма чисел после последнего найденного особого числа
minSumBetween = 0  # минимальная частичная сумма после последнего найденного особого числа
maxSumBetween = 0  # максимальная частичная сумма после последнего найденного особого числа

maxSum = 0
for x in data:

  sumTotal += x

  sumBetween += x
  minSumBetween = min(minSumBetween, sumBetween)
  maxSumBetween = max(maxSumBetween, sumBetween)

  if isSpecNumber(x):
    countSpec += 1
    sumSpec.append( sumTotal )

    tail = sumBetween - minSumBetween
    tailSpec.append( tail )

    if countSpec > K:
      prev = - 1 - K
      tailSpec[-1] = max( tail, sumSpec[-1]-sumSpec[prev]+tailSpec[prev] )

    sumBetween, minSumBetween, maxSumBetween = 0, 0, 0

  if countSpec >= K:
    maxCurrent = maxSumBetween \
               + (sumSpec[-1] - sumSpec[countSpec-K]) \
               + tailSpec[countSpec-K]
    maxSum = max( maxSum, maxCurrent )

print( maxSum )
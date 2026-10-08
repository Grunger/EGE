F = open( "27-48a.txt" )

N = int(F.readline())

sMax = 0
odd = 0
INF = 1e10
diff = [[INF, INF], [INF, INF]]
for i in range(N):
  a, b = sorted( map(int, F.readline().split()) )
  odd += b % 2
  if a % 2 != b % 2:
    diff[a % 2].append( b-a )
  sMax += b
  print(b, sMax, diff)
F.close()

even = N - odd
print( sMax, (even, odd) )

diff[0] = sorted(diff[0])[:2]
diff[1] = sorted(diff[1])[:2]

delta0 = delta1 = 0
if sMax % 2 == (even > odd):
  print( "Коррекция..." )
  print( diff[0] )
  print( diff[1] )
  if abs(even-odd) > 1:
    delta0, delta1 = diff[0][0], diff[1][0] # добавить чётное или нечётное
  elif even > odd: # even = odd + 1
    delta0 = diff[0][0] # добавить чётное
    delta1 = diff[1][0] + diff[1][1] # добавить два нечётных
  else: # odd = even + 1
    delta1 = diff[1][0] # добавить нечётное
    delta0 = diff[0][0] + diff[0][1] # добавить два чётных
  sMax -= min(delta0, delta1)

print( "Ответ:", sMax )

with open("27-64b.txt") as F:
  N = int(F.readline())
  best = [ [ (0,0), (0,0) ],
           [ (0,0), (0,0) ] ]
  for i in range(N):
    a, b = map(int, F.readline().split())
    if a % 2 == 0: continue
    if a > b: a, b = b, a
    da, db = a % 2, b % 2
    bestNew = [best[0][:], best[1][:]]
    for i in range(2):
      for j in range(2):
        prev = best[i][j]
        newSum = ( prev[0]+a, prev[1]+b )
        ii, jj = newSum[0] % 2, newSum[1] % 2
        bestNew[ii][jj] = max( bestNew[ii][jj], newSum, key=sum )
    bestNew[da][db] = max( bestNew[da][db], (a, b), key=sum )
    best = bestNew
    #print( (a, b), best )

print( best[0][1], sum(best[0][1]) )

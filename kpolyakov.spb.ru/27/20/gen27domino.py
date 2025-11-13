from random import randint

def generate( fName, N, M ):
  L = []
  last = 1
  for i in range(N):
    if randint(1,100) < 5:
      L.append( (randint(1,M), randint(1,M)) )
    else:
      L.append( (last, randint(1,M)) )
    last = L[-1][1]

  for i in range(N):
    if randint(1,100) < 50:
      L[i] = (L[i][1], L[i][0])  # flip

  with open(fName, "w") as f:
    f.write( str(N) + "\n" )
    for i in range(N):
      f.write( str(L[i][0]) + ' ' + str(L[i][1]) + '\n' )

#generate( '27-20a.txt', 20, 6 )
#generate( '27-20b.txt', 60000, 6 )
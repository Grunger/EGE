from random import randint, shuffle
N = 20
fName = '27-40b.txt'

N = 40000
fName = '27-45b.txt'

with open(fName, "w") as f:
  f.write( str(N) + '\n' )
  for i in range(N):
    #a = randint(1, 20)
    #b = randint(a+1, a+15)
    #c = randint(b+5, b+15)
    a = randint(1, 1000)
    b = randint(a+100, a+2000)
    c = randint(b+100, b+2000)
    abc = [a, b, c]
    shuffle( abc )
    f.write( str(abc[0]) + ' ' + str(abc[1]) + ' ' + str(abc[2]) + '\n' )


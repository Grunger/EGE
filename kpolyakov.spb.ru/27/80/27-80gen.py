from random import randint
N = 100
LIM = [500,900]
s = 0
with open("27-80a.txt", "w") as F:
  F.write( str(N) + "\n" )
  for i in range(N):
    x = randint(LIM[0],LIM[1])
    s += x
    F.write( str(x) + "\n" )

print(s)



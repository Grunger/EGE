f = open('27-b.txt')
n = int(f.readline())

m = [0, 0, 0]

for i in range(n):
  a = [int(x) for x in f.readline().split()]
  m1 = [0, 0, 0]
  for x in a:
    for y in m:
      ost = (x+y)%3
      if (i == 0 or y!=0) and x+y>m1[ost]:
        m1[ost]=x+y
  m = m1.copy()
print( max(m[1], m[2]) )
f.close()

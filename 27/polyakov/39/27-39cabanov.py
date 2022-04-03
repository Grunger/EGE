f = open("27-39b.txt")

n = int(f.readline())
d = dict()
for i in range(n):
	x = f.readline().strip()
	if x in d: d[x] += 1
	else: d[x] = 1

summa = 0
for i in range(100,999+1):
  s = str(i)
  s1 = s[::-1]
  if (s in d) and (s1 in d) and s!=s1:
    k = min(d[ s ], d[s1])
    summa+=2*k*sum(map(int,s))
summa = summa // 2

m = 0
for i in range(100,999+1):
  s = str(i)
  s1 = s[::-1]
  if (s in d) and (s1 in d) and s==s1:
    k = d[ s ]
    if k%2==1:
      k-=1
      m = max(m, int(s) )
    summa+=k*sum(map(int,s))

print( summa + sum(map(int,str(m))) )

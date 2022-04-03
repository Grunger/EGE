# Автор: А. Кабанов

f = open('27-64b.txt')
n = int(f.readline())
s = []
for _ in range(n):
  pair = [int(x) for x in f.readline( ).split()]
  if pair[0] % 2 != 0:
    pair.sort()
    mn, mx = pair
    cmb = [[a+mn, b+mx] for a,b in s] + s + [pair]
    s1 = [[0,0] for i in range(4)]
    for a,b in cmb:
      i = 2*(a%2)+(b%2)
      s1[i] = max(s1[i], [a,b], key=sum)
    s = s1
print(sum(s[1]))

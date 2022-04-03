# Автор: Е. Джобс

f = open('27-20b.txt')
n = int(f .readline())
s = {}
m = 0
for i in range(n):
  pair = f.readline().split()
  cmbs = [pair, pair[::-1]]
  s = {c[1]: s[c[0]] + 1 if c[0] in s else 1
       for c in cmbs}
  for c in cmbs:
    m = max(m, max(s.values()))
print(m)

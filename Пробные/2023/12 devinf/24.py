'''Определите максимальное количество идущих подряд символов в прилагаемом файле, среди которых комбинация
согласная + гласная + согласная
встречается ровно 2 раза.'''
# GBGGGGBGGGBGGGBG
from itertools import product

with open('24.txt') as f:
	s = f.read().strip()
	
m = 0
gl = 'AEU'
sogl = 'BCDF'
last = 0
queue = []
cnt = 0
for i in range(len(s) - 2):
	if s[i] in sogl and s[i + 1] in gl and s[i + 2] in sogl:
		# print(queue)
		if cnt == 2:
			if i + 2 - last > m:
				print(m, s[last - 1:i + 3], last, i, queue)
			m = max(m, i + 2 - last)
			queue.append(i + 1)
			last = queue.pop(0)
		else:
			m = max(m, i + 2 - last)
			queue.append(i + 1)
			cnt += 1
print(m)
exit(0)
# другой вариант
combs = [''.join(i) for i in product(sogl, gl, sogl)]
print(combs)
s_old = s
s = s.split(combs[0])

for c in combs:
	s_new = []
	for i in s:
		if c in i:
			s_new.extend(i.split(c))
			s.remove(i)
	s.extend(s_new)
print(s)
m = 0
for i in range(len(s) - 3):
	if len(s[i] + s[i + 1] + s[i + 2]) + 10 > m:
		m = len(s[i] + s[i + 1] + s[i + 2]) + 10
		print(m, s_old[s_old.index(s[i]) - 3:s_old.index(s[i]) + m])
print(m)
# 119

'''Определите максимальное количество идущих подряд символов в прилагаемом файле, среди которых комбинация
согласная + гласная + согласная
встречается ровно 2 раза.'''
# GBGGGGBGGGBGGGBG
with open('24_9.txt') as f:
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
			m = max(m, i + 2 - last)
			queue.append(i + 1)
			last = queue.pop(0)
		else:
			queue.append(i + 1)
			cnt += 1
print(m)

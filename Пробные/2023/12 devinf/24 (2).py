with open('24.txt') as f:
	s = f.read().strip()
	
m = 0
gl = 'AEU'
sogl = 'BCDF'
k = 0
last = 0
queue = []
cnt = 0
for i in range(len(s) - 2):
	if s[i] in sogl and s[i + 1] in gl and s[i + 2] in sogl:
	# if s[i] in gl and s[i + 1] in sogl:
		if cnt == 2:
			m = max(m, i - last)
			queue.append(i)
			if len(queue) == 3:
				last = queue.pop(0)
		else:
			queue.append(i)
			cnt += 1
	else:
		k += 1
print(m)

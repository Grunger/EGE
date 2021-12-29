f = open('24.txt')
last = 'a'
m = 0
k = 1
for i in f.read():
	if i >= last:
		k += 1
	else:
		m = max(m, k)
		k = 1
	last = i
print(m)
	

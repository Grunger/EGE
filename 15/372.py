def dell(n, m):
	return n % m == 0
	

def f(x, a):
	return (not dell(x, a)) <= ((not dell(x, 21)) and (not dell(x, 35)))
	
	
for i in range(1, 1000):
	if all(f(x, i) for x in range(1, 100000)):
		print(i)


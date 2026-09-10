def dell(n, m):
	return n % m == 0
	

def f(x, a):
	return dell(x, a) <= (not dell(x, 21) or dell(x, 35))
	
	
for i in range(1, 1000):
	if all(f(x, i) for x in range(1, 1000)):
		print(i)
		break

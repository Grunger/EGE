p = [i for i in range(10, 29 + 1)]
q = [i for i in range(13, 18 + 1)]


def f(x, a):
	return ((x in a) <= (x in p)) or (x in q)
	


a = [i for i in range(1000)]
for x in range(1000):
	if not f(x, a):
		a.remove(x)

print(a[-1] - a[0])

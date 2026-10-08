for n in range(1000):
	b = bin(n)[2:]
	if n % 4 == 0:
		b = b + b[:2]
	else:
		b = b + '100'
	r = int(b, 2)
	if r <= 166:
		print(r)
		

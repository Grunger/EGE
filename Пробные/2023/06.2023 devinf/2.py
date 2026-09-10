from itertools import product

print('z x w y')
for x, y, z, w in product((0, 1), repeat=4):
	f = (not x or y) and ((not y) ==  z) and w
	if f:
		print(z, x, w, y)

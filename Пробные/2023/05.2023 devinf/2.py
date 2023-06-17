from itertools import product

print('z x w y')
for x, y, z, w in product((0, 1), repeat=4):
	f = (not x and y) or ((not y) == (not z)) or w
	if not f:
		print(z, x, w, y)

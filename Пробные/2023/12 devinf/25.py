from fnmatch import fnmatch


for i in range(0, 10**8, 2084):
	if fnmatch(str(i), '*1?542?'):
		print(i, i // 2084)

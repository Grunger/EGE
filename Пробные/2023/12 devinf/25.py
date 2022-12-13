from fnmatch import fnmatch

#for i in range(10**10):
	#if fnmatch(str(i), '32?056*6'):
	#	print(i)
	#	break

for i in range(0, 10**8, 2084):
	if fnmatch(str(i), '*1?542?'):
		print(i, i // 2084)

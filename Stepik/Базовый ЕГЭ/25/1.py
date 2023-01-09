from fnmatch import fnmatch


for i in range(0, 10**9, 29):
    if fnmatch(str(i), '12345?7?8'):
        print(i, i // 29)

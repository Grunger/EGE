from fnmatch import fnmatch

for i in range(0, 10**10 + 1, 2023):
    if fnmatch(str(i), '32?056*6'):
        print(i, i // 2023)

from fnmatch import fnmatch


for i in range(0, 10**9, 2023):
    if fnmatch(str(i), '652*45*3'):
        print(i, i // 2023)

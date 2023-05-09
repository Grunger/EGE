from fnmatch import fnmatch

for i in range(0, 10**8, 2023):
    # print(i)
    if fnmatch(str(i), '671??1*'):
        print(i, i // 2023)

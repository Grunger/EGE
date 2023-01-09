from fnmatch import fnmatch


for i in range(0, 10**8, 19):
    if fnmatch(str(i), '12*3457'):
        print(i, i // 19)

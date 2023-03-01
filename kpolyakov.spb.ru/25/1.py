from fnmatch import fnmatch


for i in range(10**8 + 1):
    ost = (i % 117 == 0, i % 119 == 0, i % 121 == 0)
    if sum(ost) == 1 and fnmatch(str(i), '1?58*129'):
        print(i, end=' ')
        if ost[0] == 1:
            print(i // 117)
        elif ost[1] == 1:
            print(i // 119)
        else:
            print(i // 121)

from fnmatch import fnmatch


for i in range(10**9 + 1):
    ost = (i % 13, i % 17, i % 27)
    if sum(ost) == 1 and fnmatch(str(i), '*1?5424'):
        print(i, end=' ')
        if ost[0] == 0:
            print(i // 13)
        elif ost[1] == 0:
            print(i // 17)
        else:
            print(i // 27)

# 29115424 2239648
# 208125424 16009648
# 387135424 29779648
# 566145424 43549648
# 745155424 57319648
# 924165424 71089648
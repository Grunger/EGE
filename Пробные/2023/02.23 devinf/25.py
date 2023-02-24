from fnmatch import fnmatch


for i in range(10**8 + 1):
    ost = (i % 111 == 0, i % 113 == 0, i % 127 == 0)
    if sum(ost) == 1 and fnmatch(str(i), '*15*7424'):
        print(i, end=' ')
        if ost[0] == 1:
            print(i // 111)
        elif ost[1] == 1:
            print(i // 113)
        else:
            print(i // 127)

# 1587424 122109
# 15147424 1165186
# 15227424 895730
# 15457424 1189032
# 28157424 2165955
# 85157424 5009260
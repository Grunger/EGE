f = open('27A_water.txt')
n = int(f.readline())
data = [int(x) for x in f.readlines()]
# n = int(input())
# data = [int(x) for x in input().split()]
s = sum(data)
mtime = 10**10
ml, mr = 0, 0
for i in range(n):
    print(i)
    left_time = (i - 1) * 10 + sum(data[0:i])
    right_time = (n - i - 1) * 10 + sum(data[i:])
    # print(i, left_time, right_time)
    if max(left_time, right_time) <= mtime:
        mtime = max(left_time, right_time)
        ml = sum(data[0:i])
        mr = sum(data[i:])
print(mtime)
print(ml, mr)
# 66 81

f = open('27A_water.txt')
n = int(f.readline())
data = [int(x) for x in f.readlines()]
# n = int(input())
# data = [int(x) for x in input().split()]
s = sum(data)
mtime = 10**10
ml, mr = 0, 0
for left in range(s + 1):
    right = s - left
    l, r = left, right
    ltime = 0
    rtime = 0
    a = data.copy()
    k = 0
    # print(left, right)
    while left + right > 0:
        # print(left, right, a)
        if a[k] < left:
            ltime += a[k] + 10
            a[k], left = 0, left - a[k]
        elif left:
            ltime += left
            a[k], left = a[k] - left, 0
        if a[n - k - 1] < right:
            rtime += a[n - k - 1] + 10
            a[n - k - 1], right = 0, right - a[n - k - 1]
        elif right:
            rtime += right
            a[n - k - 1], right = a[n - k - 1] - right, 0
        k += 1
        if max(ltime, rtime) > mtime:
            break
    # print('time:', ltime, rtime)
    if max(ltime, rtime) < mtime:
        mtime = max(ltime, rtime)
        ml = l
        mr = r
    elif max(ltime, rtime) == mtime and l > ml:
        ml = l
        mr = r
print(mtime)
print(ml, mr)
# 66 81

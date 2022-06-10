from random import randint


def slow(n, data):
    s = sum(data)
    mtime = 10 ** 10
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
                ltime += a[k] + 5
                a[k], left = 0, left - a[k]
            elif left:
                ltime += left
                a[k], left = a[k] - left, 0
            if a[n - k - 1] < right:
                rtime += a[n - k - 1] + 5
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
    return ml


def fast(n, data):
    sum_left = sum(data) + 5 * (len(data) - 1)
    sum_right = -5
    ms = sum_left
    k = 0
    for i in range(n - 1, -1, -1):
        sum_right += 5
        for j in range(data[i]):
            sum_left -= 1
            sum_right += 1
            if max(sum_right, sum_left) < ms:
                ms = max(sum_right, sum_left)
                k = sum_left - i * 5
        sum_left -= 5
        if max(sum_right, sum_left) < ms:
            ms = max(sum_right, sum_left)
            k = sum_left - (i - 1) * 5
    return k


k = 0
while True:
    k += 1
    print(k)
    n = 20
    d = [randint(1, 100) for _ in range(20)]
    if slow(n, d) != fast(n, d):
        print(d)
        break

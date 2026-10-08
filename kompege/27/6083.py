# sum mod 11, mul mod 2310
# t 1

def slow(n, a):
    k = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % 11 == 0 and (a[i] * a[j]) % 2310 == 0:
                k += 1
    return k

def fast(n, a):
    d = 2310
    k = 0
    ost = [[0] * 11 for _ in range(d)]
    for x in a:
        x_ost = x % d
        k += ost[x % d][x % 11]

f = open('6083-27a.txt')
n = int(f.readline())
a = [int(i) for i in f]

print(slow(n, a))
# 1
# 191

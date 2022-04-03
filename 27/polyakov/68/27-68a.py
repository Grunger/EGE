f = open('27-68b.txt')
k = 3
p = 17
mnr = [[10000 for j in range(p)] for i in range(k)]
mns = 0
N = int(f.readline())
for _ in range(N):
    n1, n2, n3 = map(int, f.readline().split())
    mn = min(n1, n2, n3)
    mx = max(n1, n2, n3)
    sr = n1 + n2 + n3 - mn - mx
    mns += mn + sr
    rs = mx - mn, mx - sr
    tr = mnr.copy()
    for r in rs:
        mnr[r % k][r % p] = min(mnr[r % k][r % p], r)
        for i in range(k):
            for j in range(p):
                nr = tr[i][j] + r
                mnr[nr % k][nr % p] = min(mnr[nr % k][nr % p], nr)

if (mns % k == 0 and mns % p != 0) or (mns % k != 0 and mns % p == 0):
    print(mns)
else:
    mn = 2 * N * 10000
    for i in range(k):
        for j in range(p):
            n = mns + mnr[i][j]
            if (n % k == 0 and n % p != 0) or (n % k != 0 and n % p == 0):
                mn = min(mn, n)
    print(mn)
f.close()
f = open('27-68b.txt')
N = int(f.readline())
mx = 2 * 10000 * N
k = 3
p = 17
mns = [[0 for j in range(p)] for i in range(k)]
for st in range(N):
    n1, n2, n3 = map(int, f.readline().split())
    a = [n1 + n2, n1 + n3, n2 + n3]
    ts = [[mx + 1 for j in range(p)] for i in range(k)]
    for i in range(k):
        for j in range(p):
            if mns[i][j] < mx + 1:
                for n in a:
                    s = mns[i][j] + n
                    ts[s % k][s % p] = min(ts[s % k][s % p], s)
    mns = ts.copy()
print(min( mns[i][j] for i in range(k) for j in range(p) if (i == 0 and j != 0) or (i != 0 and j == 0) ))
f.close()
# Автор: В. Ярцев

from operator import xor
mxs = 0
mnr = [[10000 for j in range(10)] for i in range(7)]
with open('27-69b.txt') as f:
    N = int(f.readline())
    for _ in range(N):
        n1, n2, n3 = sorted(map(int, f.readline().split()))
        mxs += n2 + n3
        rs = n3 - n1, n2 - n1
        tr = mnr.copy()
        for r in rs:
            for i in range(7):
                for j in range(10):
                    nr = r + tr[i][j]
                    mnr[nr % 7][nr % 10] = min(mnr[nr % 7][nr % 10], nr)
        for r in rs:
            mnr[r % 7][r % 10] = min(mnr[r % 7][r % 10], r)
print(max( mxs - mnr[i][j] for i in range(7) for j in range(10) if xor( (mxs - mnr[i][j]) % 7 == 3, (mxs - mnr[i][j]) % 10 == 5) ))
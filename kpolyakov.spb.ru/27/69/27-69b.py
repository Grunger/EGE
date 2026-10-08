# Автор: В. Ярцев

mxs = [[0 for j in range(10)] for i in range(7)]
with open('27-69b.txt') as f:
    N = int(f.readline())
    for k in range(N):
        a = [int(n) for n in f.readline().split()]
        cmb = a[0] + a[1], a[0] + a[2], a[1] + a[2]
        ts = [[0 for j in range(10)] for i in range(7)]
        for i in range(7):
            for j in range(10):
                if k == 0 or mxs[i][j] > 0:
                    for n in cmb:
                        ns = mxs[i][j] + n
                        ts[ns % 7][ns % 10] = max(ts[ns % 7][ns % 10], ns)
        mxs = ts.copy()
print(max(y for x in mxs for y in x if (y % 7 == 3 and y % 10 != 5) or (y % 7 != 3 and y % 10 == 5)))
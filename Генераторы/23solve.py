from functools import lru_cache

# чтение файла
g = dict()
for line in open('graph.txt'):
        L, M, W = line.split()
        L, M, W = int(L), int(M), float(W)
        if L not in g:
            g[L] = dict()
        g[L][M] = W

@lru_cache(None)
def f(a, b):
        if a == b:
            return 0
        if a not in g:
            return float('inf')
        return min(g[a][c] + f(c, b) for c in g[a])

print(f(512, 355))

from functools import lru_cache

# чтение файла
g = dict()
for line in open('23_32027.txt'):
        L, M, W = line.split()
        L, M, W = int(L), int(M), float(W)
        if L not in g:
                g[L] = dict()
        g[L][M] = W

@lru_cache(None)
def f(a, b):
        if a == b:
                return 0
        # исключаем вершину 96
        if a not in g or a == 96:
                return float('inf')
        return min(g[a][c] + f(c, b) for c in g[a])

# делаем вершину 400 обязательной:
# разбиваем путь на два отрезка
print(f(1, 100))

def dfs(v, parent, color):
    color[v] = 2  # Пометить как в процессе обработки
    for to in g[v]:
        if color[to] == 1:  # Если сосед не посещён
            if dfs(to, v, color):
                return True
        elif color[to] == 2 and to != parent:  # Если сосед в процессе обработки и не родитель
            return True
    color[v] = 3  # Пометить как полностью обработанное
    return False

def has_cycle():
    color = [0] * 3  # 0: белый, 1: серый, 2: чёрный
    for i in range(3):
        if color[i] == 0:
            if dfs(i, -1, color):
                return True
    return False

# чтение файла
g = dict()
for line in open('23.txt'):
    L, M, W = line.split()
    L, M, W = int(L), int(M), float(W)
    if L not in g:
        g[L] = dict()
    g[L][M] = W
print(has_cycle())

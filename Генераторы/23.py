from random import randint, choice, choices, shuffle

k = 50  # количество вершин
n = 200  # количество ребер

g = dict()
v = set()
while len(v) < k:
    v.add(randint(1, 1000))
for c in v:
    g[c] = dict()

for i in range(n):
    L = choice(list(v))
    M = choice(list(v))
    while L == M:
        L = choice(list(v))
        M = choice(list(v))
    W = randint(1, 100_000) / 10
    g[L][M] = W
to = [i for i in g[c] for c in g]
for c in v:
    if c not in to:
        print('Исток', c)
for c in g:
    if not g[c]:
        print('Сток', c)
s = ' \t'
data = []
for L in g:
    for M in g[L]:
        W = g[L][M]
        data.append(f'{L}{''.join(choices(s, k=randint(1, 10)))}{M}{''.join(choices(s, k=randint(1, 10)))}{W}\n')
shuffle(data)
with open('23.txt', 'w') as f:
    for s in data:
        f.write(s)

from functools import lru_cache

@lru_cache(None)
def f(a, b):
    if a == b:
        return 0
    d = float('inf')
    if a not in g:
        return d
    for v, w in g[a]:
        if v == 633:
            continue
        t = w + f(v, b)
        d = min(d, t)
    return d


g = {}
for s in open('23-1.txt'):
    v1, v2, w = s.split()
    v1, v2, w = int(v1), int(v2), float(w)
    g[v1] = g.get(v1, []) + [(v2, w)]

print(f(1, 100))

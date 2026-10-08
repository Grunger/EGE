from functools import lru_cache

@lru_cache(None)
def f(a, b, ways):
    # print(a, b, ways)
    if a == b:
        return 0, ways
    d = float('inf')
    if a not in g:
        return d, ways
    for v, w in g[a]:
        # print('--', v, b, f(v, b, ways + (v, )))
        t = w + f(v, b, ways + (v, ))[0]
        if t < d:
            d = t
    return d, ways


g = {}
for s in open('23-1.txt'):
    v1, v2, w = s.split()
    v1, v2, w = int(v1), int(v2), float(w)
    g[v1] = g.get(v1, []) + [(v2, w)]

print(f(1, 100, (1, )))

from itertools import permutations

g = 'ABCG BACE CABF DEFH EBD FCD GAH HGD'
t = '156 2378 326 468 517 6134 7258 8247'
g = {k: set(w) for k, *w in g.split()}
t1 = {k: set(w) for k, *w in t.split()}

for v in permutations(g.keys()):
    t_new = t
    for a, b in zip(v, t1.keys()):
        t_new = t_new.replace(b, a)
    t2 = {k: set(w) for k, *w in t_new.split()}
    if g == t2:
        print(*zip(v, t1.keys()))

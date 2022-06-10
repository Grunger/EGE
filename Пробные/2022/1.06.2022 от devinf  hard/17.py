def divs(x):
    d = set()
    k = 1
    while k**2 <= x:
        if x % k == 0:
            d.add(k)
            d.add(x // k)
        k += 1
    return d


a = list(map(int, open('17-04-1.txt').readlines()))

m = 0
md = set()
for x in a:
    d = divs(x)
    if len(d) > m:
        m = len(d)
        md = d
print(m, md)

k = 0
m = 0
for a, b in zip(a, a[1:]):
    da = divs(a)
    db = divs(b)
    if len(md.intersection(da)) >= 3 and len(md.intersection(db)) >= 3:
        k += 1
        m = max(m, len(da.intersection(db)))

print(k, m)
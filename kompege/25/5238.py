from time import time
from fnmatch import fnmatch


def divs(n):
    d = {1, n}
    q = 2
    while q ** 2 <= n:
        if n % q == 0:
            d.add(q)
            d.add(n // q)
        q += 1
    return sum(d)


start = time()
i = 1
k = 0
while i ** 2 <= 10 ** 10:
    n = i ** 2
    if fnmatch(str(n), '7*6*1') and divs(n) % 2 == 1:
        k += 1
    i += 1
print(k)
print(time() - start)

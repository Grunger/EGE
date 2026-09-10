def is_prime(x):
    if x == 1:
        return False
    k = 2
    while k ** 2 <= x:
        if x % k == 0:
            return False
        k += 1
    return True


def divs(x):
    d = set()
    k = 1
    while k ** 2 <= x:
        if x % k == 0:
            d.add(k)
            d.add(x // k)
        k += 1
    return sorted(d)


n = 100_000_001
k = 0
while k < 5:
    div = divs(n)
    p = [i for i in div if is_prime(i)]
    e = [i for i in div if i % 2 == 0]
    # print(n, div, p, e)
    if len(p) == len(e):
        print(n, div, p, e)
        print(n, abs(sum(p) - sum(e)))
        k += 1
    n += 1
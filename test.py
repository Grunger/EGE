from fnmatch import fnmatch


def is_prime(x):
    k = 2
    while k ** 2 <= x:
        if x % k == 0:
            return False
        k += 1
    return True


def divs(x):
    d = set()
    k = 2
    while k ** 2 <= x:
        if x % k == 0:
            d.add(x // k)
            d.add(k)
        k += 1
    return sorted(d)


for i in range(10 ** 7):
    if fnmatch(str(i), '34?8*9') and sum(is_prime(a) for a in divs(i)) > 4:
        print(i, max(a for a in divs(i) if is_prime(a)))

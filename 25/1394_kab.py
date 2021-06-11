def is_simple(x):
    k = 2
    while k**2 <= x:
        if x % k == 0:
            return False
        k += 1
    return True


def a(x):
    k = 2
    divs = []
    while k**2 < x:
        if x % k == 0:
            if is_simple(k):
                divs.append(k)
            if is_simple(x // k):
                divs.append(x // k)
        k += 1
    if not divs:
        return 0
    return int(sum(divs) / len(divs))


n = 310001
count = 0
while count < 6:
    z = a(n)
    if z and z % 6 == 0 and z % 10 != 4:
        print(n, z)
        count += 1
    n += 1


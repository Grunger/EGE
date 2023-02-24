def find_divs(x):
    divs = set()
    k = 2
    while k ** 2 <= x:
        if x % k == 0:
            divs.add(k)
            divs.add(x // k)
        k += 1
    return divs


def is_simple(x):
    divs = set()
    k = 2
    while k ** 2 <= x:
        if x % k == 0:
            divs.add(k)
            divs.add(x // k)
        k += 1
        if len(divs) > 0:
            return False
    return True


x = 670001
k = 0
while k < 5:
    s = sum(i for i in find_divs(x) if is_simple(i))
    if s % 10 == 5:
        print(x, s)
        k += 1
    x += 1

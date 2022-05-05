def is_simple(x):
    if x == 1:
        return False
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def s(x):
    k = 2
    sm = 0
    while k ** 2 <= x:
        if x % k == 0:
            if is_simple(k):
                sm += k
            if is_simple(x // k):
                sm += x // k
        k += 1
    return sm


count = 0
x = 750001
while count < 5:
    sm = s(x)
    if sm and sm % 8 == 0:
        count += 1
        print(x, sm)
    x += 1





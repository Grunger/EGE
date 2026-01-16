def is_prime(n):
    if n < 2:
        return False
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True


def divs(x):
    d = []
    for i in range(2, x):
        if x % i == 0:
            d.append(i)
    return d

d = divs(5200048)
print(d)
print([i for i in d if is_prime(i)])
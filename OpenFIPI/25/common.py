def divs(n):
    d = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            d.append(i)
            d.append(n // i)
    return d


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


from fnmatch import fnmatch


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def prime_divs(x):
    i = 0
    d = []
    while x > 1:
        while x % all_prime_divs[i] == 0:
            d.append(all_prime_divs[i])
            x //= all_prime_divs[i]
        i += 1
    return d


all_prime_divs = [i for i in range(2, 10**4) if is_prime(i)]
for x in range(10**4):
    if fnmatch(str(x), '*2?2'):
        divs = prime_divs(x)
        if len(divs) == 7:
            print(x,  max(divs))

def is_prime(x):
    for k in range(2, int(x**0.5) + 1):
        if x % k == 0:
            return False
    return True

def divs(x):
    d = set()
    for k in range(2, int(x**0.5) + 1):
        if x % k == 0:
            d.add(k)
            d.add(x // k)
    return sorted(d)

c = 0
for n in range(1_103_285_717, 2_000_000_000):
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            if is_prime(k) and is_prime(n // k):
                if '16' in str(k) and '16' in str(n // k):
                    print(n, k)
                    c += 1
                    break
    if c == 5:
        break
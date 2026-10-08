# Нахождение делителей числа
# 10: 1 2 5 10
# 18: 1 2 3 6 9 18
# 20: 1 2 4 5 10 20
# 17: 1 17
# 9: 1 3 9
def divs(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


k = 0
for x in range(500_001, 1_000_000):
    d = divs(x)
    for i in d:
        if i % 10 == 8 and i != 8 and i != x:
            print(x, i)
            k += 1
            break
    if k == 5:
        break

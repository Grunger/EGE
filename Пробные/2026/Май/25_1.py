def divs(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


k = 0
for i in range(6_700_001, 7_900_000):
    d = divs(i)
    m = min(d) + max(d) if d else 0
    if m % 100 == 26:
        c = len([j for j in d if is_prime(j)])
        if m % c == 0:
            print(i, m)
            k += 1
    if k == 5:
        break
# 7800233 1114326
# 7800248 3900126
# 7800269 106926
# 7800605 1560126
# 7800669 2600226

#6700105 1340026
#6700453 113626
#6700569 2233526
#6700869 2233626
#6701048 3350526
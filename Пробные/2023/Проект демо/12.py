def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for n in range(100):
    if is_prime(117 + n * 4):
        print(n)
        break

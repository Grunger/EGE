def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


a = '0123456789ABCDEFGH'
k = 0
for x in a:
    n = int(f'56{x}3', 18) + int(f'4{x}9', 18) - int(f'57{x}1', 18)
    if is_prime(n):
        k += 1
print(k)

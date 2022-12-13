s = '0123456789abcdefgh'


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for x in s:
    a = int(f'56{x}3', 18) + int(f'{x}4{x}9', 18) - int(f'57{x}1', 18)
    if is_prime(a):
        print(x)
# 997

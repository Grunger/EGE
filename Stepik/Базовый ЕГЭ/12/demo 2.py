def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for n in range(1, 100):
    s = '>' + '0' * 39 + '2' * 39
    s = s + '1' * n
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    s = s.replace('>', '')
    s = sum(int(i) for i in s)
    if is_prime(s):
        print(n)
        break
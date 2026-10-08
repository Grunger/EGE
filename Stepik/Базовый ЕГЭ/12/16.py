def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

k = 0
for n in range(10, 100):
    s = '1' + '0' * n
    while '10' in s:
        if '10' in s:
            s = s.replace('10', '001', 1)
        if '1' in s:
            s = s.replace('1', '01', 1)

    if is_prime(len(s)):
        k += 1
        print(n, s, len(s))
print(k)

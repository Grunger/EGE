def f(n):
    n -= n % 4
    n = bin(n)[2:]
    if n.count('1') % 2 == 1:
        n += '1'
    else:
        n += '0'
    if n.count('1') % 2 == 1:
        n += '1'
    else:
        n += '0'
    return int(n, 2)


for i in range(1, 100):
    if f(i) > 100:
        print(f(i))
        break


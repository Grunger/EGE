def f(n):
    n = bin(n)[2:]
    for _ in range(3):
        if n.count('0') == n.count('1'):
            n += n[-1]
        else:
            if n.count('0') < n.count('1'):
                n += '0'
            else:
                n += '1'
    return int(n, 2)


for i in range(80, 100):
    r = f(i)
    # print(i, r)
    if r % 2 == 0 and r % 4 != 0:
        print(i)

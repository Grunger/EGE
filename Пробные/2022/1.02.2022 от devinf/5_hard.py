for n in range(1000):
    r = bin(n)[2:][::-1]
    if r.startswith('0'):
        r = '1' + r
    r += bin(n)[2:]
    if int(r, 2) <= 6000:
        print(n)



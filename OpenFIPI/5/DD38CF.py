for n in range(0, 100):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[:3]
    else:
        k = bin((n % 3) * 3)[2:]
        s = s + k
    r = int(s, 2)
    if r < 76:
        print(n)

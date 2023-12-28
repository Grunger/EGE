res = []
for n in range(1, 1000):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += b[-2:]
    else:
        b = b + bin(n % 3)[2:]
        if n % 3 == 2:
            b = b + bin(n % 3)[2:]
    r = int(b, 2)
    res.append(r)
print(min(i for i in res if i > 100))

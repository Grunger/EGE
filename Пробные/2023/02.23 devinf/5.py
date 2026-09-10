ab = set()
for a in range(100, 1000):
    for b in range(100, 1000):
        x1 = a // 100 + b // 100
        x2 = a // 10 % 10 + b // 10 % 10
        x3 = a % 10 + b % 10
        s = int(str(x3) + str(x1) + str(x2))
        s = s // 10 % 1000
        ab.add(s)
        if s == 2:
            print(a, b, s)
print(ab)

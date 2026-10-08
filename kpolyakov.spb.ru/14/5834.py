for i in range(131058, 131058 + 1):
    n = hex(i)[2:]
    if i % 2 == 0:
        n = n + 'f'
    else:
        n = n + '0'
    for st in range(2):
        s = 0
        for c in n:
            s += int(c, 16)
        n = n + hex(s % 16)[2:]
    if n.count(max(n)) == 5 * n.count(min(n)):
        print(i, n)
        break

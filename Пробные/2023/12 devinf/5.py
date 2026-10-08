r = []
for i in range(1, 100):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = '1' + n
        n = n[:-2] + '01'
    else:
        n = n + '10'
        n = '1' + n[2:]
    r.append(int(n, 2))
print(max(i for i in r if i < 100))

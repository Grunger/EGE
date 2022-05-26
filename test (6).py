rez = set()
for x in range(1, 100):
    for y in range(1, 100):
        r = (55 + 2 * 5 ** x) * 5 ** x + 55 + 5 ** y
        s = []
        while r > 0:
            s.append(r % 5)
            r = r // 5
        rez.add(sum(s))
print(rez)

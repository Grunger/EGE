def divs(x):
    s = set()
    for i in range(2, x):
        if x % i == 0:
            s.add(i)
    return sorted(s)


for i in range(251487, 251513 + 1):
    d = divs(i)
    if len(d) == 2:
        print(d)

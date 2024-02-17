def one(s):
    d = dict()
    for c in set(s):
        d[c] = s.count(c)
    max_c = [c for c in d if d[c] == max(d.values())]
    min_c = [c for c in d if d[c] == min(d.values())]
    for i in max_c[:-1]:
        s = s.replace(i, max_c[-1])
    for i in min_c[:-1]:
        s = s.replace(i, min_c[-1])
    return s.count(max_c[-1] + min_c[-1]) + s.count(min_c[-1] + max_c[-1])


def two(s):
    k = 0
    d = dict()
    for c in set(s):
        d[c] = s.count(c)
    max_c = [c for c in d if d[c] == max(d.values())]
    min_c = [c for c in d if d[c] == min(d.values())]
    # print(min_c, max_c)
    for i in range(len(s) - 1):
        if s[i] in max_c and s[i + 1] in min_c or s[i] in min_c and s[i + 1] in max_c:
            k += 1
    return k


s = open('24_2715.txt').read().strip()
print(one(s))
print(two(s))


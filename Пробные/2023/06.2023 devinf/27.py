from itertools import product

def slow():
    mx_k = 0
    mx_s = 0
    mask = list(product((0, 1), repeat=n))
    print(mask)
    for item in mask:
        s = 0
        for i in range(n):
            if item[i] == 1:
                s += a[i]
        if s % 23 == 0 and s > mx_s:
            mx_s = s
            mx_k = sum(item)
    return mx_s, mx_k


def fast():
    s = sum(a)
    min_s = {i: 10**10 for i in range(23)}
    min_k = {i: 0 for i in range(23)}
    for x in a:
        new_min_s = min_s.copy()
        for i in range(23):
            ost = (x + min_s[i]) % 23
            if x + min_s[i] < min_s[ost] or x + min_s[i] == min_s[ost] and min_k[x % 23] + min_k[i] < min_k[ost]:
                new_min_s[ost] = x + min_s[i]
                min_k[ost] = 1 + min_k[i]
        min_s = new_min_s
        if x <= min_s[x % 23]:
            min_s[x % 23] = x
            min_k[x % 23] = 1
        # print(x, min_k)
    # print(s % 23)
    # print(s)
    # print(min_s)
    # print(min_k)
    return s - min_s[s % 23], n - min_k[s % 23]


f = open('27_A.txt')
n = int(f.readline())
a = [int(i) for i in f]
print(slow())
#print(fast())

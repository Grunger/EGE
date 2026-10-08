ans = []
for n in range(1, 100):

    b = bin(n)[2:]
    s = b.count('1')
    if s % 3 == 0:
        b = b + b[:2]
    else:
        b = bin((s % 3) * 3)[2:] + b
    r = int(b, 2)
    if r <= 60:
        ans.append(n)
    # print(n, r)
print(max(ans))

k = 0
for i in range(10**8):
    x = i
    l, m = 0, 0
    while x > 0:
        l += 1
        if x % 12 == 0:
            m += 1
        x //= 12
    if l == 6 and m == 0:
        k += 1
    if l == 7:
        break
print(k)
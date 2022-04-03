k = 0
for i in range(10000):
    s = i
    s //= 7
    n = 1
    while s < 255:
        s += n
        n += 1
    if n == 7:
        print(i)
        k += 1
print(k)

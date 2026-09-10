k = 0
for i in range(1000):
    s = i
    n = 1
    while s >= 5:
        s = s - 15
        n = n * 2
    if n == 2048:
        k += 1
print(k)

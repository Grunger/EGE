#for x in range(97129744, 0, -1):
m = 0
for x in range(1, 3000):
    a = 9 * 11 ** 350 + 8 * 11 ** 150
    a -= x
    k = 0
    while a:
        if a % 11 == 0:
            k += 1
        a //= 11
    if k == 202:
        print(x)


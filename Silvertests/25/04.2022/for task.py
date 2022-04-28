# 346?456?, делящиеся на число 117 без остатка.

for b in range(10, 100):
    k = 0
    for i in range(10):
        for j in range(10):
            n = f'390{i}{j}451'
            if int(n) % b == 0:
                k += 1
                # print(n, int(n) // b)
    if k == 5:
        print(b)



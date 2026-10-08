# 1?345?7?8, делящиеся на число 117 без остатка.

b = 117
for i in range(10):
    for j in range(10):
        for k in range(10):
            n = f'1{i}345{j}7{k}8'
            if int(n) % b == 0:
                print(n, int(n) // 117)



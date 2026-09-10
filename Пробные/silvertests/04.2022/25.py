# 270?5?41, делящиеся на число 21 без остатка.

for i in range(10):
    for j in range(10):
        n = int(f'270{i}5{j}43')
        if n % 21 == 0:
            print(n, n // 21)
# 123*456?

b = 109
for i in range(10):
    n = int(f'123456{i}')
    if n % b == 0:
        print(n, n // b)
for i in range(100):
    for j in range(10):
        n = int(f'123{i}456{j}')
        if n % b == 0:
            print(n, n // b)

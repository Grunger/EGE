for i in range(10):
    for j in range(10):
        n = int(f'12345{i}7{j}8')
        if n % 23 == 0:
            print(n, n // 23)
for x in '0123456789abcde':
    a = int(f'1{x}51', 15) - int(f'3{x}2', 15)
    if a % 4 == 0:
        print(a, a // 4)
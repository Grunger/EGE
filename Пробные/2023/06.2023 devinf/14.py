for x in '0123456789abcde':
    a = int(f'67845{x}65', 15) + int(f'1{x}23456', 15)
    if a % 14 == 0:
        print(x, a, a // 14)

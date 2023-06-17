for n in range(1, 10000000):
    b = bin(n)[2:]  # двоичная запись
    if n % 2 != 0:
        # замена 0 на 1, 1 на 0
        b = b.replace('0', '2').replace('1', '0').replace('2', '1')
    b = ''.join([i * 2 for i in b])  # удвоение каждой цифры числа
    r = int(b, 2)
    if r > 60:
        print(n)
        break

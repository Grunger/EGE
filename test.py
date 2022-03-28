def ma_c81(x):
    m = 0
    while x:
        m = max(m, x % 8)
        x //= 8
    return m == 6


ma_c8 = lambda x: max(int(i) for i in oct(x)[2:]) == 6
print(oct(71), ma_c8(71))
print(oct(200), ma_c8(200))
print(oct(310), ma_c8(310))
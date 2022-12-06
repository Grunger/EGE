k = 0
for n in range(1, 101):
    s = '1' + '0' * n
    while '10' in s or '1' in s:
        if '10' in s:
            s = s.replace('10', '0001', 1)
        else:
            s = s.replace('1', '0', 1)
    if len(s) % 7 == 0:
        k += 1
print(k)

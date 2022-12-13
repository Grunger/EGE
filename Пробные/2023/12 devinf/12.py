
for n in range(1, 101):
    s = '0' * n + '1'
    while '01' in s:
        if '1' in s:
            s = s.replace('1', '10', 1)
        if '01' in s:
            s = s.replace('01', '100', 1)
    print(n, len(s), s)

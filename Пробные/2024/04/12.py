m = 0
for n in range(4, 1000):
    s = '2' + '9' * n
    while '29' in s or '69' in s or '999' in s:
        s = s.replace('29', '9', 1)
        s = s.replace('69', '92', 1)
        s = s.replace('999', '6', 1)
    s = sum(int(i) for i in s)
    m = max(m, s)
print(m)

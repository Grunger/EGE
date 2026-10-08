s = '>' + '1' * 100 + '2' * 50 + '0' * 80
while '10' in s or '20' in s:
    while '>2' in s:
        s = s.replace('>2', '1>', 1)
    print(s)
    while '>1' in s:
        s = s.replace('>1', '2>', 1)
    print(s)
    while '>0' in s:
        s = s.replace('>0', '0>', 1)
    print(s)
    s = s.replace('10', '2', 1)
    s = s.replace('20', '1', 1)
print(s.count('2'))
# 145

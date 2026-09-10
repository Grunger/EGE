s = '1' + '0' * 105
while '10' in s:
    if '100' in s:
        s = s.replace('100', '1011', 1)
    else:
        s = s.replace('10', '11', 1)
print(s)
s = int(s, 2)
print(s)
s = hex(s)[2:]
print(s)
print(sum(int(i, 16) for i in s))

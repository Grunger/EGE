s = '8' * 2022
while '1111' in s or '8888' in s:
    if '1111' in s:
        s = s.replace('1111', '88888', 1)
    else:
        s = s.replace('8888', '18', 1)
print(s)

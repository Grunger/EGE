s = '4' * 40 + '7' * 40 + '9' * 40
while '47' in s or '49' in s or '97' in s:
    if '47' in s:
        s = s.replace('47', '74', 1)
    if '49' in s:
        s = s.replace('49', '94', 1)
    if '97' in s:
        s = s.replace('97', '79', 1)
print(s[24] + s[72] + s[104])
# 120
# 7: 1 40
# 9: 41: 80
# 4: 81: 120
s = 'AAAG' * 2022
while 'AAA' in s or 'GG' in s:
    if 'AAA' in s:
        s = s.replace('AAA', 'GGGG', 1)
    else:
        s = s.replace('GG', 'A', 1)
    if 'AG' in s:
        s = s.replace('AG', 'GA', 1)
print(s)

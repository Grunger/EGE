from itertools import product

k = 0
for s in product('ЕИОРТЯ', repeat=6):
    if s[0] not in 'РТЯ' and s.count('И') >= 2 and 'ИИ' not in ''.join(s):
        k += 1
print(k)

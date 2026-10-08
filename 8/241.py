from itertools import permutations


vovels = 'АИ'
consonants = 'МКТ'
k = set()
for i in permutations('АММИАКАТ'):
    if any(i[j] in vovels and i[j + 1] in vovels or i[j] in consonants and i[j + 1] in consonants for j in range(7)):
        k.add(i)
print(len(k))

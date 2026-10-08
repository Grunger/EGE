from itertools import product


for i, word in enumerate(product('АБРТЫ', repeat=5), start=1):
    if 'Ы' not in word and 'АА' not in ''.join(word):
        print(i)
        break

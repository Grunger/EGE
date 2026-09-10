from itertools import permutations

s = 'МОЛОКО'
k = 0
for i in permutations(s, r=5):
    print(i)

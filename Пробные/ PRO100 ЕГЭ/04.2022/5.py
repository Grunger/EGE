from itertools import permutations

for i in range(100, 1000):
    a = []
    for j in permutations(str(i), r=2):
        if int(''.join(j)) > 9:
            a.append(int(''.join(j)))
    print(i, a)
    if max(a) - min(a) == 5:
        print(i, a)
        break
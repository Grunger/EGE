from itertools import product

s = 'ABCDE'
gl = 'AE'
sogl = 'BCD'
k = 0
for i in product(s, repeat=4):
    if i[-1] in sogl and i[1] in 'ABC' and i[0] != i[1] and ((i[0] in gl) != (i[2] in gl)):
        k += 1
print(k)

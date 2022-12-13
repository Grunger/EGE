from itertools import product


s = 'ABCDE'
sogl = 'BCD'
gl = 'AE'
k = 0
for item in product(s, repeat=4):
    x = ''.join(item)
    if x[-1] in sogl and x[1] in 'ABC' and x[0] != x[1] and (x[0] in sogl and x[2] in gl or x[0] in gl and x[2] in sogl):
        k += 1
print(k)

print(7 * 2 * 3 + 5 * 3 * 3)

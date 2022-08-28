from itertools import product

gl = 'AO'
sogl = 'CDF'

pairs = []
for i in product(sogl, gl):
    pairs.append(''.join(i))
print(pairs)
with open('24.txt') as f:
    mx = 0
    s = f.readline().strip()
    for start in range(2):
        k = 0
        for i in range(start, len(s) - 1, 2):
            if s[i] + s[i + 1] in pairs:
                k += 1
            else:
                mx = max(k, mx)
                k = 0
    print(mx)

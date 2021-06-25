f = open('27-b.txt')
n = int(f.readline())
s = {i: {0: [0, 0]} for i in range(5)}
for i in range(n):
    x = int(f.readline())
    cmb = [x + b for a in s[i % 5].values() for b in a]
    s[i % 5] = {a % 7: [x, a - x] for a in sorted(cmb + [k for j in s[i % 5].values() for k in j])}
print(s)
sums = [s[i][0] for i in s if 0 in s[i]]
print(*sorted(sums, key=lambda x: x[0] + x[1])[-1])

f = open('27-B.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 0
r = 321
s = [0] * r
for x in a:
    ost = x % r
    s_new = [0] * r
    for i in range(r):
        if s[i] != 0:
            s_new[(i + ost) % r] = s[i]
    s = s_new[:]
    s[ost] += 1
    k += s[0]
print(k)

# 4516 5711890064
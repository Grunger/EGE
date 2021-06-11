f = open('files/27-B_1396_kab.txt')
n = int(f.readline())
s = 0
min_d_odd = 100000
min_d_even = 100000
for i in f.readlines():
    i = [int(j) for j in i.split()]
    s += min(i)
    d = [max(i) - min(i), sum(i) - max(i) - 2 * min(i)]
    if any(i < 0 for i in d):
        print(d)
    min_d_odd = min(min_d_odd, min([i for i in d if (2553076273 + i) % 123 and i % 2], default=10000))
    min_d_even = min(min_d_even, min([i for i in d if (2553076273 + i) % 123 and i % 2 == 0 and i > 0], default=10000))
print(s)
print(s % 123)
print(min_d_odd)
print(min_d_even)
print(s + min_d_odd)
# 2553076273
# 82
# 123
# 246

# 2553076396
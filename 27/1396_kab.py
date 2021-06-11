f = open('files/27-B_1396_kab.txt')
n = int(f.readline())
f = f.readlines()
s = {0: 0}
for i in [[int(i.split()[0]), int(i.split()[1]), int(i.split()[2])] for i in f]:
    s = {x % 123: x for x in sorted([a + b for a in i for b in s.values()], reverse=True)}
s[0] = 10**10
print(min([i for i in s.values() if i % 2 == 0]))

# print(min([i for i in s.values()]))

# 2553076478

# 2553076396

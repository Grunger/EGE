s = open('24_1428_kab.txt').read().strip()
# ZZZZXYZZZXYZ
s = s.split('XY')
s1 = []
for item in s:
    s1.extend(item.split('XZ'))
print(max([len(i) for i in s1]))
print([(i, s1[i]) for i in range(len(s1)) if len(s1[i]) == 23])
print(len(s1))

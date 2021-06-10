f = open('27v20_B.txt').readlines()
n = int(f.pop(0))
s = {0: 0}
for i in [[int(i.split()[0]), int(i.split()[1])] for i in f]:
    s = {x % 65: x for x in sorted([a + b for a in i for b in s.values()], reverse=True)}
s[0] = 10**10
print(min(s.values()))

# 300018 334066293
#        334058877

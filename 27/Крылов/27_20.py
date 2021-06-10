f = open('files/27v20_B.txt').readlines()
n = int(f.pop(0))
f = [[int(i.split()[0]), int(i.split()[1])] for i in f]
s = 0
min_d = 10000
for i in f:
    s += min(i)
    min_d = min(min_d, abs(i[0] - i[1]))
if s % 65 == 0:
    s += min_d
print(s)

# 300018 334066293
#        334058877
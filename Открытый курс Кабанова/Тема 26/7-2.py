f = open('7_27B.txt')
n = int(f.readline())
m = 0
s = [0]
for i in range(n):
    x = int(f.readline())
    s = [x + a for a in s] + [x]
    s = list({x % 1000: x for x in sorted(s)}.values())
    m = max([m] + [i for i in s if i % 1000 == 0])
    print(x, s)
print(m)
# 6
# 997
# 3
# 4
# 12
# 88
# 1900
f = open('files/27v13_B.txt')
n = int(f.readline())
s = 0
min_d = 10**10
for item in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    if abs(a - b) % 55:
        min_d = min(min_d, abs(a - b))
if s % 55 == 0:
    s += min_d
print(s)

# 357333 333648796

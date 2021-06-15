f = open('files/27v19_B.txt')
n = int(f.readline())
s = 0
min_d = 10**10
for item in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    if abs(a - b) % 67:
        min_d = min(min_d, abs(a - b))
if s % 67 == 0:
    s += min_d
print(s)

# 336852 334912275

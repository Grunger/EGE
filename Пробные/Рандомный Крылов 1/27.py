f = open('27v01_B.txt')
n = int(f.readline())
s = 0
min_d = 10**10
for i in range(n):
    a, b = list(map(int, f.readline().split()))
    s += max(a, b)
    if abs(a - b) % 31:
        min_d = min(abs(a - b), min_d)
print(s)
print(s % 31)
print(s - min_d)

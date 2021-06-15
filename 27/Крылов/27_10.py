f = open('files/27v10_B.txt')
n = int(f.readline())
s = 0
min_d = 10**10
for item in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    if abs(a - b) % 49:
        min_d = min(min_d, abs(a - b))
if s % 49 == 0:
    s -= min_d
print(s)

# 357333 661782863


f = open('27-3a.txt')
n = int(f.readline())
s = 0
min_d = [10000] * 3
for i in range(n):
    a, b = map(int, f.readline().split())
    print(abs(a - b), abs(a - b) % 3)
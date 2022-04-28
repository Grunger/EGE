f = open('27-1B.txt')
n, k = map(int, f.readline().split())
d = {i: None for i in range(1, k + 1)}
m = 10 ** 10
flag = False
# 1000000
for i in range(n):
    if i % 100000 == 0:
        print(i)
    x = int(f.readline())
    d[x] = i
    if not flag and all(d[a] is not None for a in d):
        flag = True
    if flag:
        m = min(m, i - min(d.values()) + 1)
    # print(f'{x=} {m=} {d=}')
print(m)

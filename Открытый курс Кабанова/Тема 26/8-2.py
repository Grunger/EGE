f = open('8_27_B.txt')
n = int(f.readline())
ms = [None] * 3
s = 0
m = 0
k = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if x % 5 == 0:
        k += 1
    if k % 3 == 0:
        m = max(m, s)
    elif ms[k % 3] is not None:
        m = max(m, s - ms[k % 3])
    if ms[k % 3] is None:
        ms[k % 3] = s
    # print(f'{x=} {k=} {s=} {m=} {ms=}')
print(m)
# 7
# 20
# 5
# 4
# 10
# 6
# 15
# 8
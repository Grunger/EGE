f = open('9_27_B.txt')
n = int(f.readline())
s = 0
r = 69
m = 0
ln = 10**10
ms = [(0, 0)] + [None] * (r - 1)
for i in range(n):
    x = int(f.readline())
    s += x
    ost = s % r
    if ms[ost] is not None:
        if s - ms[ost][0] >= m:
            # print(f'!!! {x=}, {s=}, {m=} {ln=} {ms=}')
            if s - ms[ost][0] > m:
                m = s - ms[ost][0]
            ln = i - ms[ost][1]
    if ms[s % r] is None:
        ms[s % r] = (s, i)
    # print(f'{x=}, {s=}, {m=} {ln=} {ms=}')
print(m, ln)

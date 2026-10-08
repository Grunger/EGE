#f = open('26_18_26134.txt')
f = open('26_t.txt')
n, d = map(int, f.readline().split())
# d = 5
# 77
print(d - 128)
spot0 = []
spot1 = []
for line in f:
    r, t = map(int, line.split())
    if t == 0:
        spot0.append(r)
    else:
        spot1.append(r)
spot0.sort()
spot1.sort()
i0 = i1 = 0
# a = [spot0[30]]
a = [spot0[0]]
while i0 < len(spot0) - 1 and i1 < len(spot1) - 1:
    while spot1[i1] < a[-1] + d and i1 < len(spot1) - 1:
        i1 += 1
    if spot1[i1] >= a[-1] + d:
        a.append(spot1[i1])
    while spot0[i0] < a[-1] + d and i0 < len(spot0) - 1:
        i0 += 1
    if spot0[i0] >= a[-1] + d:
        a.append(spot0[i0])
print(len(a))
print(a)
i0 = i1 = 0
# a = [spot1[11]]
a = [spot1[0]]
while i0 < len(spot0) - 1 and i1 < len(spot1) - 1:
    while spot0[i0] < a[-1] + d and i0 < len(spot0) - 1:
        i0 += 1
    if spot0[i0] >= a[-1] + d:
        a.append(spot0[i0])
    while spot1[i1] < a[-1] + d and i1 < len(spot1) - 1:
        i1 += 1
    if spot1[i1] >= a[-1] + d:
        a.append(spot1[i1])

print(len(a))
print(a)

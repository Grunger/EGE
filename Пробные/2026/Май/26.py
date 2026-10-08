f = open('1_26.txt')
n = int(f.readline())
d = dict()
sr = 0
for line in f:
    art, price, m = map(int, line.split())
    sr += price
    if art in d:
        if m == 1:
            d[art] = [price, d[art][1], d[art][2] + 1]
        else:
            d[art] = [price, d[art][1] + 1, d[art][2]]
    else:
        if m == 1:
            d[art] = [price, 0, 1]
        else:
            d[art] = [price, 1, 0]
sr = sr / n
lid1 = 0
k1 = 0
v1 = 0
min1 = 0
lid2 = 0
k2 = 0
v2 = 0
min2 = 0
for art in d:
    p, m1, m2 = d[art]
    if p > sr:
        if m1 > k1 or m1 == k1 and m2 < min1:
            k1 = m1
            lid1 = art
            v1 = m1 * p
            min1 = m2
    else:
        if m1 > k2 or m1 == k2 and m2 < min2:
            k2 = m1
            lid2 = art
            v2 = m1 * p
            min2 = m2
print(sr)
print(abs(v1 - v2))
print(min(min1, min2))


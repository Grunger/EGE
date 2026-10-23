def dist(p1, p2):
    x1, y1, e1, t1 = p1
    x2, y2, e2, t2 = p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def center(c):
    cnt = 0
    m = 10**10
    for p1 in c:
        s = 0
        for p2 in c:
            s += abs(p1[-2] - p2[-2])
        if s < m:
            m = s
            cnt = p1
    return cnt

f = open('27_31521.txt')
clusters = [[], [], [], []]
r = 2.0
for line in f:
    x, y, vx, vy, m, t = line.replace(',', '.').split()
    x, y, vx, vy, m = map(float, [x, y, vx, vy, m])
    e = 1/2 * m * (vx**2 + vy**2)
    p = (x, y, e, t)
    if e < 4:
        clusters[0].append(p)
    elif e < 6:
        clusters[1].append(p)
    elif e < 9:
        clusters[2].append(p)
    else:
        clusters[3].append(p)
mx = 0
for c in clusters:
    for p1 in c:
        for p2 in c:
            if p1[-1] == 'II' and p2[-1] == 'II':
                d = dist(p1, p2)
                mx = max(mx, d)
print(mx * 10000)

for c in clusters:
    print(center(c))
    print(center(c)[-2] * 10000)

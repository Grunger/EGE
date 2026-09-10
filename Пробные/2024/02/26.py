f = open('26.txt')
n = int(f.readline())
m = [[int(t.split()[0]), int(t.split()[1])] for t in f]
m.sort(key=lambda x: (x[1], x[0]))


k = 0
cur_last = 0
way = []
d = 5
for i in range(n):
    if m[i][0] >= cur_last + d:
        k += 1
        cur_last = m[i][1] + d
        way.append(m[i])
        print(m[i])

print(k)
for i in range(n):
    if m[i][0] >= way[-2][0]:
        print(m[i], m[i][0] - way[-2][1])


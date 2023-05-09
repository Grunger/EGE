f = open('26_ege_2022.txt')
n = int(f.readline())
data = sorted([int(i) for i in f])
for i in range(11):
    data.pop(0)
mx = 0
cur = [data.pop(0)]
for b in data:
    if b - cur[-1] >= 11:
        cur.append(b)
print(len(cur))
print(cur[0])
# 854

# f = open('26_t.txt')
f = open('26_23208.txt')
n = int(f.readline())
shl = []
okr = []
d = dict()
d_shl = dict()
d_okr = dict()
i = 1
for line in f:
    s, o = map(int, line.split())
    shl.append(s)
    okr.append(o)
    d[i] = (s, o)
    d_shl[s] = i
    d_okr[o] = i
    i += 1
a = sorted(shl + okr)
lenta = [0] * n
l = 0
r = n - 1
k_shl = 0
done = set()
last = 0
for i in range(2 * n):
    d = a[i]  # время шлифовки или окрашивания
    if d in shl:
        num = d_shl[d]
    else:
        num = d_okr[d]
    if num in done:
        continue
    if d in shl:
        lenta[l] = num
        l += 1
    else:
        lenta[r] = num
        r -= 1
    done.add(num)
    last = num
    if d in shl:
        k_shl += 1
print(last, k_shl)
# print(lenta)


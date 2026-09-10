f = open('6_27B.txt')
n = int(f.readline())
r = 10
k = {i: 0 for i in range(10)}
for i in range(n):
    x = int(f.readline())
    k1 = k.copy()
    k1[x % r] += 1
    for j in range(r):
        k1[(x + j) % r] += k[j]
    k = k1.copy()
    # print(x, k)
print(k[5])

# 4
# 8
# 7
# 12
# 23
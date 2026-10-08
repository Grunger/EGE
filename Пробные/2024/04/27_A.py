f = open('27_B.txt')
n = int(f.readline())
data = [int(i) for i in f]
mn = 10 ** 9
for i in range(n // 2):
    j = i + n // 2
    st = 0
    for k in range(n):
        dist_a = min(abs(k - i), abs(i + n - k), abs(k + n - i))
        dist_b = min(abs(k - j), abs(j + n - k), abs(k + n - j))
        if dist_a < dist_b:
            st += dist_a * data[k]
        else:
            st += dist_b * data[k]
        # print(k, st, dist_a, dist_b)
    print('---', i, j, st)
    mn = min(mn, st)
print(mn)
# 80297

f = open('27B_water.txt')
n = int(f.readline())
data = [int(x) for x in f.readlines()]

sum_left = sum(data) + 10 * (len(data) - 1)
sum_right = -10
ms = sum_left
k = 0
for i in range(n - 1, -1, -1):
    # print(i)
    sum_left -= 10 + data[i]
    sum_right += 10 + data[i]
    if max(sum_right, sum_left) < ms:
        ms = max(sum_right, sum_left)
        k = sum_left - (i - 1) * 10

print(ms)
print(k, sum(data) - k)

# 63 84
# 25015197 25013362

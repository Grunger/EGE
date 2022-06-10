f = open('27B_water.txt')
n = int(f.readline())
data = [int(x) for x in f.readlines()]

# n = int(input())
# data = [int(x) for x in input().split()]

sum_left = sum(data) + 5 * (len(data) - 1)
sum_right = -5
ms = sum_left
k = 0
for i in range(n - 1, -1, -1):
    sum_right += 5
    for j in range(data[i]):
        sum_left -= 1
        sum_right += 1
        if max(sum_right, sum_left) < ms:
            ms = max(sum_right, sum_left)
            k = sum_left - i * 5
    sum_left -= 5
    if max(sum_right, sum_left) < ms:
        ms = max(sum_right, sum_left)
        k = sum_left - (i - 1) * 5

print(ms)
print(k, sum(data) - k)

# 66 81
# 25014637 25013922
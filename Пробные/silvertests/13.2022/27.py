f = open('27.txt')
n = int(f.readline())
data = []
for i in range(n):
    data.append(int(f.readline()))

# count = 0
# k = 21
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (data[i] * data[j]) % k == 0:
#             # print(data[i], data[j])
#             count += 1
# print(count)

k = 0
k3 = 0
k7 = 0
k21 = 0
count = 0
for i in data:
    if i % 21 == 0:
        k21 += 1
        count += k
    elif i % 7 == 0:
        k7 += 1
        count += k3 + k21
    elif i % 3 == 0:
        k3 += 1
        count += k7 + k21
    else:
        count += k21
    k += 1
print(count)
# 7266296

from random import randint


f = open('27_B.txt')
n = int(f.readline())
data = []
for i in range(n):
    data.append(int(f.readline()))

# p = 0
# k = 15
# k2 = 45
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (data[i] * data[j]) % k == 0 and (data[i] * data[j]) % k2 != 0:
#             p = max(p, data[i] * data[j])
# print(p)

m3 = 0
m5 = 0
m15 = 0
m = 0
for i in data:
    if i % 15 == 0 and i % 45 != 0 and i > m15:
        m15 = i
    elif i % 5 == 0 and i % 15 != 0 and i > m5:
        m5 = i
    elif i % 3 == 0 and i % 9 != 0 and i > m3:
        m3 = i
    if i % 3 != 0:
        m = max(m, i)
        m0 = m

m = max(m15 * m, m3 * m5)
print(m)


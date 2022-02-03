f = open('27_B.txt')
n = int(f.readline())
data = []
for i in range(n):
    data.append(int(f.readline()))
# p = 0
# k = 21
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (data[i] * data[j]) % k == 0:
#             p = max(p, data[i] * data[j])
# print(p)
m3 = 0
m7 = 0
m21 = 0
m = 0
for i in data:
    if i % 21 == 0 and i > m21:
        m21 = i
    elif i % 7 == 0 and i > m7:
        m7 = i
    elif i % 3 == 0 and i > m3:
        m3 = i
    else:
        m = max(m, i)
m = max(m21 * m, m3 * m7)
print(m)

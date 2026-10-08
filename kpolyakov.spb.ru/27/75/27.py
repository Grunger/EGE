# Дана последовательность из N натуральных чисел.
# Рассматриваются все её непрерывные подпоследовательности,
# такие что сумма элементов каждой из них кратна k = 43.
# Найдите среди них подпоследовательность с максимальной суммой,
# определите её длину. Если таких подпоследовательностей найдено несколько,
# в ответе укажите количество элементов самой короткой из них.

f = open('27-75b.txt')
n = int(f.readline())

s = []
r = 43
m = (0, 0)
for i in range(n):
    x = int(f.readline())
    s = [(x + a[0], a[1] + 1) for a in s] + [(x, 1)]
    s = {x[0] % r: (x[0], x[1]) for x in sorted(s, key=lambda x: (x[0], -x[1]))}
    if 0 in s:
        if s[0][0] > m[0]:
            m = s[0]
        elif s[0][0] == m[0] and s[0][1] < m[1]:
            m = s[0]
    s = s.values()
print(m)
# data = [int(i) for i in f]
# ln = n
# m = 0
# r = 43
# for i in range(n):
#     for j in range(i, n):
#         s = 0
#         for k in range(i, j + 1):
#             s += data[k]
#         if s % r == 0 and s >= m:
#             if s == m and j - i + 1 < ln:
#                 ln = j - i + 1
#             elif s > m:
#                 m = s
#                 ln = j - i + 1
# print(ln)



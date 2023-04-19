'''
139
В файле записана последовательность натуральных чисел. Назовём парой любые два
числа из последовательности, расстояние между которыми не менее 25.
Расстоянием называется разность номеров элементов последовательности.
Необходимо определить количество пар, в которых сумма чисел в паре делится без остатка на 4,
а их произведение – на 9009.
'''

# n, *a = map(int, open('27-139a.txt').read().split())
# k = 0
# for i in range(n):
#     for j in range(i + 25, n):
#         if (a[i] + a[j]) % 4 == 0 and (a[i] * a[j]) % 9009 == 0:
#             k += 1
# print(k)
s = 2
p = 10
n, *a = map(int, open('27-T.txt').read().split())

k = 0
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % s == 0 and (a[i] * a[j]) % p == 0:
            k += 1
            # print(a[i], a[j])
print(k)

divs = [i for i in range(1, p + 1) if p % i == 0]
t = [{d: 0 for d in divs} for _ in range(s)]
k = 0
for x in a:
    print(x)
    s_ost = (s - x % s) % s
    for d in divs:
        if x * d % p == 0:
            k += t[s_ost][p // d]
            t[(s - s_ost) % s][p // d] += 1
    print(t)
    print(k)
print(k)

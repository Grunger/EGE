# Дана последовательность N целых положительных чисел. Рассматриваются все пары элементов последовательности,
# в которых только одно число кратно 23. Порядок элементов в паре неважен.
# Среди всех таких пар нужно найти и вывести минимальную сумму элементов пары.

def slow():
    ans = 10**10
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (a[i] % 23 == 0) != (a[j] % 23 == 0):
                ans = min(ans, a[i] + a[j])
    return ans


def fast():
    mn = 10 ** 10
    mn23 = 10**10
    for x in a:
        if x % 23 == 0:
            mn23 = min(mn23, x)
        else:
            mn = min(mn, x)
    return mn + mn23


f = open('27_B.txt')
n = int(f.readline())
a = [int(i) for i in f]
# print(slow())
print(fast())


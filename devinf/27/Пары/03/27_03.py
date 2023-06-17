# Рассматриваются все пары элементов последовательности, разность которых чётна, и в этих парах,
# по крайней мере, одно из чисел пары делится на 19. Порядок элементов в паре неважен.
# Среди всех таких пар нужно найти и вывести максимальную сумму элементов пары.


def slow():
    mx = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (a[i] - a[j]) % 2 == 0 and (a[i] % 19 == 0 or a[j] % 19 == 0):
                mx = max(mx, a[i] + a[j])
    return mx


def fast():
    mx_odd = 0
    mx_odd19 = 0
    mx_even = 0
    mx_even19 = 0
    ans = 0
    for x in a:
        if x % 2 == 0:
            if x % 19 == 0:
                ans = max(ans, x + mx_even, x + mx_even19)
                mx_even19 = max(x, mx_even19)
            else:
                ans = max(ans, x + mx_even19)
                mx_even = max(x, mx_even)
        else:
            if x % 19 == 0:
                ans = max(ans, x + mx_odd, x + mx_odd19)
                mx_odd19 = max(x, mx_odd19)
            else:
                ans = max(ans, x + mx_odd19)
                mx_even = max(x, mx_odd)
    return ans


f = open('27_B.txt')
n = int(f.readline())
a = [int(i) for i in f]
# print(slow())
print(fast())

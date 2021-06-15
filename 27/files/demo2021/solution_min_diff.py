# Имеется набор данных, состоящий из пар положительных целых чисел.
# Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех выбранных чисел
# не делилась на 3 и при этом была максимально возможной. Гарантируется, что искомую сумму
# получить можно. Программа должна напечатать одно число – максимально возможную сумму,
# соответствующую условиям задачи.

# 32 127127 399762080


f = open('27-B.txt')
n = int(f.readline())
s = 0
min_d = 10000
for item in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    if abs(a - b) % 3:
        min_d = min(min_d, abs(a - b))
if s % 3 == 0:
    s -= min_d
print(s)

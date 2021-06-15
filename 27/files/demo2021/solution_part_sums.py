# Имеется набор данных, состоящий из пар положительных целых чисел.
# Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех выбранных чисел
# не делилась на 3 и при этом была максимально возможной. Гарантируется, что искомую сумму
# получить можно. Программа должна напечатать одно число – максимально возможную сумму,
# соответствующую условиям задачи.

# 32 127127 399762080


f = open('27-B.txt')
n = int(f.readline())
s = {0: 0}
for i in range(n):
    pair = list(map(int, f.readline().split()))
    sums = sorted(a + b for a in s.values() for b in pair)
    s = {x % 3: x for x in sums}
s[0] = 0
print(max(s.values()))
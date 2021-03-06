# Имеется набор данных, состоящий из пар положительных целых чисел.
# Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех
# выбранных чисел НЕ оканчивалась на 5 и при этом была максимально возможной.
# Гарантируется, что искомую сумму получить можно. Программа должна напечатать
# одно число – максимально возможную сумму, соответствующую условиям задачи.

# 44 13159 40799380


f = open('27-23b.txt')
n = int(f.readline())
s = {0: 0}
for i in range(n):
    pair = list(map(int, f.readline().split()))
    sums = sorted([a + b for a in s.values() for b in pair])
    s = {x % 10: x for x in sums}
s[5] = -1
print(s)
print(max(s.values()))

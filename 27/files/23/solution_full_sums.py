# Имеется набор данных, состоящий из пар положительных целых чисел.
# Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех
# выбранных чисел НЕ оканчивалась на 5 и при этом была максимально возможной.
# Гарантируется, что искомую сумму получить можно. Программа должна напечатать
# одно число – максимально возможную сумму, соответствующую условиям задачи.

# 44 13159 40799380


f = open('27-23a.txt')
n = int(f.readline())
s = [0]
for i in range(n):
    pair = list(map(int, f.readline().split()))
    sums = [a + b for a in s for b in pair]
    s = sums.copy()
    print(i)
print('s:', max([i for i in s if i % 10 != 5]))
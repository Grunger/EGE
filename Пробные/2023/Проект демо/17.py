# Определите количество пар последовательности, в которых
# только одно число оканчивается на 3, а сумма квадратов элементов пары
# не меньше квадрата максимального элемента последовательности,
# оканчивающегося на 3

data = list(map(int, open('17.txt').read().strip().split('\n')))
m3 = max([i for i in data if abs(i) % 10 == 3])
ans = []
for a, b in zip(data, data[1:]):
    a, b = abs(a), abs(b)
    if ((a % 10 == 3) and (b % 10 != 3) or (a % 10 != 3) and (b % 10 == 3)) and\
            a ** 2 + b ** 2 >= m3 ** 2:
        ans.append(a ** 2 + b ** 2)
print(len(ans))
print(max(ans))

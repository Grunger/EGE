# оба числа оканчиваются на ту же цифру, что и максимальное число последовательности, кратное 7

a = list(map(int, open('17-04-1.txt').readlines()))

k = 0
m = 0
m25 = max(i for i in a if i % 92 == 0)
for a, b in zip(a, a[1:]):
    if bool(m25 % sum(int(i) for i in str(a))) + bool(m25 % sum(int(i) for i in str(b))) == 1:
        k += 1
        m = max(m, a + b)

print(k, m)

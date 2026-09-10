# сумма элементов пары в восьмеричной системе счисления содержит столько же разрядов,
# что и максимальное число последовательности, кратное 76

def ln8(x):
    k = 0
    while x:
        k += 1
        x //= 8
    return x


a = list(map(int, open('17-04-1.txt').readlines()))
k = 0
m = 0
m76 = ln8(max(i for i in a if i % 76 == 0))

for a, b in zip(a, a[1:]):
    if ln8(a + b) == m76:
        k += 1
        m = max(m, a + b)
print(k, m)

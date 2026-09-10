# хотя бы одно число кратно минимальному числу последовательности, кратному 25

a = list(map(int, open('17-04-1.txt').readlines()))

k = 0
m = 0
m25 = min(i for i in a if i % 25 == 0)
for a, b in zip(a, a[1:]):
    if a % m25 == 0 or b % m25 == 0:
        k += 1
        m = max(m, a + b)

print(k, m)

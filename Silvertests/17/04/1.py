# хотя бы одно число превышает максимальное число последовательности, кратное 97

a = list(map(int, open('17-04-1.txt').readlines()))

k = 0
m = 10**9
m97 = max(i for i in a if i % 97 == 0)
for a, b in zip(a, a[1:]):
    if a > m97 or b > 97:
        k += 1
        m = min(m, a + b)

print(k, m)

f = open('17.txt')
a = [int(i) for i in f]
m123 = min(i for i in a if i % 123 == 0)
ans = []
for a, b in zip(a, a[1:]):
    if (a % 2023 >= m123) != (b % 2023 >= m123):
        ans.append(a + b)
print(len(ans), max(ans))

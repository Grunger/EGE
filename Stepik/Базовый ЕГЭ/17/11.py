f = open('17.txt')
data = [int(i) for i in f]
k = min(i for i in data if abs(i) % 10 == 8)
ans = []
for a, b in zip(data, data[1:]):
    if ((abs(a) % 10 == 7) != (abs(b) % 10 == 7)) and (a + b) ** 2 >= k ** 2:
        ans.append(a**2 + b**2)
print(len(ans), max(ans))

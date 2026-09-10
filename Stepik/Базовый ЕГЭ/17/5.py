f = open('17_1.txt')
data = [int(i) for i in f]
max6 = max(i for i in data if i % 6 == 0)
ans = []
for a, b in zip(data, data[1:]):
    if (a % 5 == 0 or b % 5 == 0) and a + b <= max6:
        ans.append(a + b)
print(len(ans), max(ans))

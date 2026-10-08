data = list(map(int, open('17-1.txt').readlines()))


k26 = max([i for i in data if str(i)[-2:] == '26'])
k = 0
m = 0
for i in range(len(data) - 1):
    a, b = abs(data[i]), abs(data[i + 1])
    if a * b % 26 == 0 and data[i] + data[i + 1] <= k26:
        k += 1
        m = max(m, (data[i] - data[i + 1]) ** 2)
print(k, m)
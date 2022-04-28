data = list(map(int, open('17-1.txt').readlines()))


k = 0
for i in range(len(data) - 1):
    a, b = abs(data[i]), abs(data[i + 1])
    if data[i] <= data[i + 1] and any(a % i == 0 and b % i == 0 for i in (2, 5, 7)):
        k += 1
print(k)
k2 = 0
for i in range(len(data) - 1):
    a, b = abs(data[i]), abs(data[i + 1])
    if data[i] <= data[i + 1] and any(a % i == 0 and b % i == 0 for i in (2, 5, 7)):
        if data[i + 1] - data[i] > k:
            k2 += 1
print(k2)

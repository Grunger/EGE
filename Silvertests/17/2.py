data = list(map(int, open('17-1.txt').readlines()))

k = 0
m = 0
for i in range(len(data) - 2):
    a, b, c = abs(data[i]), abs(data[i + 1]), abs(data[i + 2])
    if len([i for i in (a % 5, b % 5, c % 5) if i == 0]) == 2:
        k += 1
        if (data[i] + data[i + 1] + data[i + 2]) % 3 == 0:
            m = max(m, data[i] + data[i + 1] + data[i + 2])
print(k, m)

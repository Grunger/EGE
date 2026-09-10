data = list(map(int, open('17-1.txt').readlines()))


k123 = min([i for i in data if abs(i) % 123 == 0])
k = 0
s = 0
for i in range(len(data) - 2):
    a, b, c = abs(data[i]), abs(data[i + 1]), abs(data[i + 2])
    if data[i] >= k123 and data[i + 1] >= k123 and data[i + 2] >= k123 and abs(data[i] + data[i + 1] + data[i + 2]) % 100 == 22:
        k += 1
        s += max(data[i], data[i + 1], data[i + 2])
print(k, s)

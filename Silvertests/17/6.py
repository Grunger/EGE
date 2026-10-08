data = list(map(int, open('17-1.txt').readlines()))


k = 0
s = set()
for i in range(len(data) - 2):
    a, b, c = abs(data[i]), abs(data[i + 1]), abs(data[i + 2])
    if data[i] >= data[i + 1] >= data[i + 2] and (data[i] + data[i + 1] > data[i + 2])and (data[i] + data[i + 2] > data[i + 1]) and (data[i + 2] + data[i + 1] > data[i]):
        k += 1
        s = s.union({i, i + 1, i + 2})
print(k, len(s))

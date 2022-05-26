data = [int(i) for i in open('17.txt').readlines()]
k = 0
m = 0
for i in range(1, len(data) - 1):
    if data[i - 1] > data[i] < data[i + 1]:
        k += 1
        m = max(m, abs(data[i - 1] - data[i]))
        m = max(m, abs(data[i + 1] - data[i]))
if data[0] < data[1]:
    k += 1
    m = max(m, abs(data[0] - data[1]))
if data[-1] < data[-2]:
    k += 1
    m = max(m, abs(data[-1] - data[-2]))
print(k, m)

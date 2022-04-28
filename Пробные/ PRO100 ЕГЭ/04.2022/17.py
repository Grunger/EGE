f = open('17.txt')
data = [int(i) for i in f]
k = 0
m = 0
for i in range(len(data) - 2):
    c = 0
    for j in range(3):
        if data[i + j] > 0 and data[i + j] % 10 == 9:
            c += 1
    if c == 1 and data[i + 1] > 0 and data[i + 1] % 10 == 9:
        k += 1
        m = max(m, data[i] + data[i + 1] + data[i + 2])
print(k, m)

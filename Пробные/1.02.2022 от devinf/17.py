data = [int(i) for i in open('17.txt').readlines()]
k = 0
m = 0
for i in data:
    if len(str(i)) > 1 and str(i)[-1] == str(i)[-2] and i > m:
        m = i
sums = []
for i in range(len(data) - 1):
    if data[i] % 5 == 0 or data[i] % 7 == 0 or data[i + 1] % 5 == 0 or data[i + 1] % 7 == 0:
        if (data[i] + data[i + 1]) <= m:
            k += 1
            sums.append(data[i] + data[i + 1])
print(k, max(sums))

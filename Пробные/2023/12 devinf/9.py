with open('9.csv') as f:
    k = 0
    for line in f:
        data = [int(i) for i in line.split(';')]
        if (max(data) + min(data)) ** 2 > sum([i ** 2 for i in data]) - max(data) ** 2 - min(data) ** 2 or any(data.count(i) == 3 for i in data) and len(set(data)) == 4:
            k += 1
print(k)
# 4209

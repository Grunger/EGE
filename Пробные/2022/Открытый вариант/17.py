f = open('107_17.txt')
data = [int(i) for i in f]
m21 = min(i for i in data if i % 21 == 0)
k, m = 0, 0
for a, b in zip(data, data[1:]):
    if a % m21 == 0 or b % m21 == 0:
        k += 1
        m = max(m, a + b)
print(k, m)

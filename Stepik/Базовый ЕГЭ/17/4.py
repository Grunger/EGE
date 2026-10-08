f = open('17_5.txt')
data = [int(i) for i in f]
min21 = min(i for i in data if i % 21 == 0)
ans = []
for a, b in zip(data, data[1:]):
    if a % min21 == 0 or b % min21 == 0:
        ans.append(a + b)
print(len(ans), max(ans))

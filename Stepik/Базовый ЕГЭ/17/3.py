f = open('17_1.txt')
data = [int(i) for i in f]
ans = []
for a, b in zip(data, data[1:]):
    if a % 2 == 0 or b % 2 == 0:
        ans.append(a + b)
print(len(ans), max(ans))

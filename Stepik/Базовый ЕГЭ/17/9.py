f = open('17_4.txt')
data = [int(i) for i in f]
k = min(data)
ans = []
for a, b in zip(data, data[1:]):
    if a % 111 == k or b % 111 == k:
        ans.append(a + b)
print(len(ans), min(ans))

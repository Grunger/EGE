data = [int(i) for i in open('17.txt').read().split()]
mn8 = min(i for i in data if i % 8 == 0 and i != 8)
ans = []
for a, b in zip(data, data[1:]):
    if a % mn8 == 0 and b % mn8 == 0:
        ans.append((a, b))
print(len(ans))
print(ans)
ans = min(ans, key=lambda x: x[0] + x[1])
print(ans)

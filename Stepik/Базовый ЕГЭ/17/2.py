f = open('17_1.txt')
a = [int(i) for i in f]
ans = []
for x in a:
    if abs(x) % 10 in (3, 6):
        ans.append(x)
print(len(ans), max(ans))

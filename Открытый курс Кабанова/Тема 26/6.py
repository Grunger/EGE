f = open('6_27_0.txt')
n = int(f.readline())
s = []
r = 10
count = 0
for i in range(n):
    x = int(f.readline())
    s.extend([x + a for a in s] + [x])

    s = {x % r: x for x in sorted(s)}
    s = list(s.values())
    count += len([a for a in s if a % 10 == 5])
    print(x, [a for a in s if a % 10 == 5])
print(count)

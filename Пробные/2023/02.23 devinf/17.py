data = [int(i) for i in open('17.txt').read().split()]
mx1 = max([i for i in data if abs(i) % 10 == 2])
k = 0
mx = 0
for x in data:
    if x % 3 == 0 and x % 17 != 0 and x % 7 != 0 and mx1 % abs(x) == 0:
        k += 1
        mx = max(mx, x)
print(k, mx)

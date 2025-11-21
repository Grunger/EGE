n = int(input())
k = 0
s = 0
for i in range(n):
    x = int(input())
    if x % 7 == 5:
        k += 1
        s += x
if k == 0:
    print('NO')
else:
    print(s / k)

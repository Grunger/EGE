n = int(input())
m = -10000
for i in range(n):
    x = int(input())
    if x % 7 % 2 != 0:
        if x > m:
            m = x
if m == -10000:
    print('NO')
else:
    print(m)

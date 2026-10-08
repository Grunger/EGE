m = 100_000
x = int(input())
while x != 0:
    if x % 9 == 1:
        if x < m:
            m = x
    x = int(input())
if m != 100_000:
    print(m)
else:
    print('NO')

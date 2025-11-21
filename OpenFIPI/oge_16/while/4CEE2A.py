s = 0
x = int(input())
while x != 0:
    if x % 5 % 2 == 0:
        s += x
    x = int(input())
if s > 0:
    print(s)
else:
    print('NO')

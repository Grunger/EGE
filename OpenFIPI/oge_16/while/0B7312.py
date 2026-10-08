s = 0
x = int(input())
while x != 0:
    if x % 7 == 3:
        s += x
    x = int(input())
if s > 0:
    print(s)
else:
    print('NO')

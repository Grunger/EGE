k = 0
s = 0
x = int(input())
while x != 0:
    if 10 <= x <= 99:
        k += 1
        s += x
    x = int(input())
if k > 0:
    print(round(s / k, 1))
else:
    print('NO')

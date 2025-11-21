k = 0
s = 0
x = int(input())
while x != 0:
    if 100 <= x <= 999:
        k += 1
        s += x
    x = int(input())
if k > 0:
    print(s / k)
else:
    print('NO')

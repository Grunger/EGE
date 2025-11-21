k = 0
x = int(input())
while x != 0:
    if x % 5 % 2 != 0:
        k += 1
    x = int(input())
if k > 0:
    print(k)
else:
    print('NO')

n = int(input())
s = 0
for i in range(n):
    x = int(input())
    if x % 7 == 3:
        s += x
if s == 0:
    print('NO')
else:
    print(s)

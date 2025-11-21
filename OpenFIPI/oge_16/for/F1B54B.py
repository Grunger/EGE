n = int(input())
k = 0
for i in range(n):
    x = int(input())
    if x % 7 == 1:
        k += 1
if k == 0:
    print('NO')
else:
    print(k)

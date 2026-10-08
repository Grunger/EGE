k = 0
for i in range(8):
    x = int(input())
    if x % 3 == 0 and x % 10 == 4:
        k += 1
print(k)

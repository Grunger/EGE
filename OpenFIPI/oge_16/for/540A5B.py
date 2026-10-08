s = 0
for i in range(5):
    x = int(input())
    if x % 4 == 0 and x % 10 == 6:
        s += x
print(s)

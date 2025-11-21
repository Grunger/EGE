s = 0
x = int(input())
while x != 0:
    if x % 4 == 0 or x % 9 == 0:
        s += x
    x = int(input())
print(s)


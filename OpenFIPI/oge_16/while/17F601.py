s = 0
x = int(input())
while x != 0:
    if 100 <= x <= 999 and x % 4 == 0:
        s += x
    x = int(input())
print(s)

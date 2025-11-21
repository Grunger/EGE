s = 0
x = int(input())
while x != 0:
    if x % 7 == 0 and x % 10 == 0:
        s += x
    x = int(input())
print(s)


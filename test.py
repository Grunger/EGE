s = 0
x = int(input())
while x != 0:
    if x % 6 == 0 and x % 10 == 8:
        s += x
    x = int(input())
print(s)

def move(x):
    if x % 2 == 0:
        return x - 1, x // 2
    return x - 1,


s = [0] * 1000
for i in range(20):
    if i <= 12:
        s[i] = 5
for i in range(100):
    if s[i] == 0 and any(s[a] == 5 for a in move(i)):
        s[i] = 1
for i in range(100):
    if s[i] == 0 and all(s[a] == 1 for a in move(i)):
        s[i] = -1
for i in range(100):
    if s[i] == 0 and any(s[a] == -1 for a in move(i)):
        s[i] = 2
for i in range(100):
    if s[i] == 0 and all(s[a] in (1, 2) for a in move(i)):
        s[i] = -2
for i in range(101):
    print(i, s[i])

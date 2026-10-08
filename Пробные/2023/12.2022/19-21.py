def move(s):
    rest = 60
    if s <= rest // 2:
        return s + 1, s + 2, s * 2
    if s <= rest - 2:
        return s + 1, s + 2
    return s + 1


s = [0] * 100
for i in range(100):
    if i >= 51:
        s[i] = 5
for i in range(100):
    if s[i] == 0 and any(s[j] == 5 for j in move(i)):
        s[i] = 1
for i in range(100):
    if s[i] == 0 and all(s[j] == 1 for j in move(i)):
        s[i] = -1
for i in range(100):
    if s[i] == 0 and any(s[j] == -1 for j in move(i)):
        s[i] = 2
for i in range(100):
    if s[i] == 0 and all(s[j] in (1, 2) for j in move(i)):
        s[i] = -2
for i in range(100):
    if s[i] == 0 and any(s[j] in (-1, -2) for j in move(i)):
        s[i] = 3
for i in range(100):
    if s[i] == 0 and all(s[j] in (1, 2, 3) for j in move(i)):
        s[i] = -3
for i in range(51):
    print(i, s[i])

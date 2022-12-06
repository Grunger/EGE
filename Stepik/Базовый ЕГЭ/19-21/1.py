def move(h):
    return h + 1, h * 2


s = [0] * 100
for i in range(100):
    if i >= 25:
        s[i] = 5
for i in range(50):
    if s[i] == 0 and any(s[j] == 5 for j in move(i)):
        s[i] = 1
for i in range(50):
    if s[i] == 0 and all(s[j] == 1 for j in move(i)):
        s[i] = -1
for i in range(50):
    if s[i] == 0 and any(s[j] == -1 for j in move(i)):
        s[i] = 2
for i in range(50):
    if s[i] == 0 and all(s[j] in (1, 2) for j in move(i)):
        s[i] = -2
for i in range(25):
    print(i, s[i])

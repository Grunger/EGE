def move(h):
    return h + 1, h + 3, h * 2


s = [0] * 1000
win = 442
for i in range(1000):
    if i >= win:
        s[i] = 5

for i in range(500):
    if s[i] == 0 and any(s[a] == 5 for a in move(i)):
        s[i] = 1
for i in range(500):
    if s[i] == 0 and all(s[a] == 1 for a in move(i)):
        s[i] = -1
for i in range(500):
    if s[i] == 0 and any(s[a] == -1 for a in move(i)):
        s[i] = 2
for i in range(500):
    if s[i] == 0 and all(s[a] in (1, 2) for a in move(i)):
        s[i] = -2
for i in range(win):
    if s[i] in (-1, 2, -2):
        print(i, s[i])
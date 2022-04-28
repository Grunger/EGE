def move(h):
    return h + 1, h + 4, h * 2


win = 35
s = [0] * 500
for i in range(500):
    if i >= win and i % 2 != 0:
        s[i] = 5

# win 1
for i in range(win):
    if s[i] == 0 and any(s[a] == 5 for a in move(i)):
        s[i] = 1
# lose 1
for i in range(win):
    if s[i] == 0 and all(s[a] == 1 or a >= win and a % 2 == 0 for a in move(i)):
        s[i] = -1
# win 2
for i in range(win):
    if s[i] == 0 and any(s[a] == -1 for a in move(i)):
        s[i] = 2
# lose 2
for i in range(win):
    if s[i] == 0 and all(s[a] in (1, 2) or a >= win and a % 2 == 0 for a in move(i)):
        s[i] = -2
for i in range(win):
    print(i, s[i])

def moves(h):
    return h + 2, h + 5, h * 3


s = [0] * 1000
win = 27
for i in range(win):
    if any(j >= win for j in moves(i)):
        s[i] = 1
for i in range(win):
    if s[i] == 0 and all(s[j] == 1 for j in moves(i)):
        s[i] = -1
for i in range(win):
    if s[i] == 0 and any(s[j] == -1 for j in moves(i)):
        s[i] = 2
for i in range(win):
    if s[i] == 0 and all(s[j] > 0 for j in moves(i)):
        s[i] = -2
for i in range(win):
    print(i, s[i])

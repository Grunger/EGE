def moves(h):
    if h % 2 == 0:
        return h - 1, h - 2, h // 2
    return h - 1, h - 2


s = [0] * 1000
win = 10
for i in range(100):
    if i <= win:
        s[i] = 5
for i in range(100):
    if s[i] == 0 and any(s[j] == 5 for j in moves(i)):
        s[i] = 1
for i in range(100):
    if s[i] == 0 and all(s[j] == 1 for j in moves(i)):
        s[i] = -1
for i in range(100):
    if s[i] == 0 and any(s[j] == -1 for j in moves(i)):
        s[i] = 2
for i in range(100):
    if s[i] == 0 and all(s[j] > 0 for j in moves(i)):
        s[i] = -2
for i in range(win, 50):
    print(i, s[i])

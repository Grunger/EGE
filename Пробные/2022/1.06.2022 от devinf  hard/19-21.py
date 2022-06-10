def moves(h):
    return h + 2, h + 4, h * 2


s = [0] * 1000
s1 = [0] * 1000
win = 125
lose = 163

for i in range(win):
    if any(lose >= j >= win for j in moves(i)):
        s[i] = 1
        s1[i] = 1
for i in range(win):
    if s[i] == 0 and all(s[j] == 1 or j > lose for j in moves(i)):
        s[i] = -1
for i in range(win):
    if s[i] == 0 and any(s[j] == -1 for j in moves(i)):
        s[i] = 2
for i in range(win):
    if s[i] == 0 and all(s[j] > 0 or j > lose for j in moves(i)):
        s[i] = -2

for i in range(win):
    if s1[i] == 0 and any(s1[j] == 1 or j >= lose for j in moves(i)):
        s1[i] = -1
for i in range(win):
    if s1[i] == 0 and any(s1[j] == -1 for j in moves(i)):
        s1[i] = 2
for i in range(win):
    if s1[i] == 0 and all(s1[j] > 0 or j >= lose for j in moves(i)):
        s1[i] = -2

for i in range(win):
    if s[i] in (-2, -1, 1, 2):
        print(i, s[i])

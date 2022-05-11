def move(x):
    return x + 1, x * 2


def win(x):
    return 20 <= x <= 30


pos = [0] * 40
# выигрышные за 1 ход
for s in range(1, 19 + 1):
    if any(win(h) for h in move(s)):
        pos[s] = 1
# проигрышные за 1 ход (all - выигрышная стратегия, any - неудачный ход
for s in range(1, 19 + 1):
    if pos[s] == 0 and all(pos[h] == 1 or h > 30 for h in move(s)):
        pos[s] = -1
# выигрышные за 2 хода
for s in range(1, 19 + 1):
    if pos[s] == 0 and any(pos[h] == -1 for h in move(s)):
        pos[s] = 2
# проигрышные за 2 хода
for s in range(1, 19 + 1):
    if pos[s] == 0 and all(pos[h] > 0 or h > 30 for h in move(s)):
        pos[s] = -2
print('s p')
print(*[(s, p) for s, p in enumerate(pos[:20])], sep='\n')
# 19 - 5
# 20 - 9 17
# 21 - 16

def move(x):
    return x + 1, x * 2


def win(x):
    return 50 <= x <= 70


pos = [0] * 140
# выигрышные за 1 ход
for s in range(1, 140):
    if any(win(h) for h in move(s)):
        pos[s] = 1
# проигрышные за 1 ход (all - выигрышная стратегия, any - неудачный ход
for s in range(1, 49 + 1):
    if pos[s] == 0 and all(pos[h] == 1 or h > 70 for h in move(s)):
        pos[s] = -1
# выигрышные за 2 хода
for s in range(1, 49 + 1):
    if pos[s] == 0 and any(pos[h] == -1 for h in move(s)):
        pos[s] = 2
# проигрышные за 2 хода
for s in range(1, 49 + 1):
    if pos[s] == 0 and all(pos[h] > 0 or h > 70 for h in move(s)):
        pos[s] = -2
print('s p')
print(*[(s, p) for s, p in enumerate(pos[:49 + 1])], sep='\n')


# 1 куча
# +1 *3
# 1 <= s <= 64 
# win 65

def turn(x):
    return x + 1, x * 3


def win(x):
    return 65 <= x <= 100


pos = [0 for i in range(500)] 

# победа в 1 ход
for i in range(500):
    if any(win(h) for h in turn(i)):
        pos[i] = 1
# проигрыш первым ходом. (any Для первого вопроса)
for i in range(65):
    if all(pos[i] == 0 and (pos[h] == 1 or h > 100) for h in turn(i)):
        pos[i] = -1
# победа в 2 хода
for i in range(65):
    if any(pos[i] == 0 and pos[h] == -1 for h in turn(i)):
        pos[i] = 2
# проигрыш 2 ходом
for i in range(65):
    if all(pos[i] == 0 and (pos[h] in (1, 2) or h > 100) and ((pos[h] in (1, 2)) != (h > 100)) for h in turn(i)):
        pos[i] = -2

print(*enumerate(pos[:65]), sep='\n')


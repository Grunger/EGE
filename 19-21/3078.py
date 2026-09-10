# 1 куча
# +2 +3 *2
# 1 <= s <= 29 
# win 30

def turn(x):
    return x + 2, x + 3, x *2


def win(x):
    return x >= 30


pos = [0 for i in range(500)] 

# победа в 1 ход
for i in range(500):
    if any(win(h) for h in turn(i)):
        pos[i] = 1
# проигрыш первым ходом.
for i in range(30):
    if all(pos[i] == 0 and (pos[h] == 1) for h in turn(i)):
        pos[i] = -1
# победа в 2 хода
for i in range(30):
    if any(pos[i] == 0 and pos[h] == -1 for h in turn(i)):
        pos[i] = 2
# проигрыш 2 ходом
for i in range(30):
    if all(pos[i] == 0 and (pos[h] in (1, 2)) for h in turn(i)):
        pos[i] = -2

print(*enumerate(pos[:30]), sep='\n')


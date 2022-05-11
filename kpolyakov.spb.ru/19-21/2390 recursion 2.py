# 2 кучи
# +1 *2
# 8, 1 <= s <= 66
# win 75
win = 75
end = 67
first = 8
d = {}


def turn(h):
    x, y = h
    return (x + 1, y), (x * 2, y), (x, y + 1), (x, y * 2)


def f(h):
    x, y = h
    if h in d:
        return d[h]
    # 0 - признак победы
    if x + y >= win:
        d[h] = 0
        return 0
    # хотя бы один ход победный за 1 ход
    if any(f(i) == 0 for i in turn(h)):
        d[h] = 1
        return 1
    # для 19 any (не выигрышная стратегия)
    if all(f(i) == 1 for i in turn(h)):
        d[h] = 2
        return 2
    if any(f(i) == 2 for i in turn(h)):
        d[h] = 3
        return 3
    if all(f(i) in (1, 3) for i in turn(h)):
        d[h] = 4
        return 4
    d[h] = -1
    return -1


# 0 - для просчетов победы
# 1 - победа первым ходом (Победа Пети за 1 ход)
# 2 - проигрыш первым ходом (Победа Вани за 1 ход)
# 3 - победа вторым ходом (Победа Пети за 1 ход)
# 4 - проигрыш первым или вторым ходом (Победа Вани за 1 или 2 хода)
# # 19
# for s in range(1, end):
#     if f((first, s)) == 2:
#         print(19, s, sep='\t')
# 20
# for s in range(1, end):
#     if f((first, s)) == 3:
#         print(20, s, sep='\t')
# 21
for s in range(1, end):
    if f((first, s)) == 4:
        print(21, s, sep='\t')

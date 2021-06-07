# 2 кучи
# +1 *2
# 8, 1 <= s <= 66
# win 75
win = 75
end = 67
first = 8
d = {}


def turn(x, y):
    return (x + 1, y), (x * 2, y), (x, y + 1), (x, y * 2)


def f(x, y):
    if (x, y) in d:
        return d[(x, y)]
    # 0 - признак победы
    if x + y >= win:
        d[(x, y)] = 0
        return 0
    # хотя бы один ход победный за 1 ход
    if any(f(i, j) == 0 for i, j in turn(x, y)):
        d[(x, y)] = 1
        return 1
    # для 19 any (не выигрышная стратегия)
    if all(f(i, j) == 1 for i, j in turn(x, y)):
        d[(x, y)] = 2
        return 2
    if any(f(i, j) == 2 for i, j in turn(x, y)):
        d[(x, y)] = 3
        return 3
    if all(f(i, j) in (1, 3) for i, j in turn(x, y)):
        d[(x, y)] = 4
        return 4
    d[(x, y)] = -1
    return -1


# # 19
# for s in range(1, end):
#     if f(first, s) == 2:
#         print(19, s, sep='\t')
# 20
# for s in range(1, end):
#     if f(first, s) == 3:
#         print(20, s, sep='\t')
# 21
for s in range(1, end):
    if f(first, s) == 4:
        print(21, s, sep='\t')

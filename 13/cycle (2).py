# s = ['АБГ', 'БД', 'ВАБДГЖ', 'ГЖ', 'ДЗЕК', 'ЕВКИ', 'ЖЕ', 'ЗК', 'ИЖ', 'КИ']
# s = ['АБВ', 'БГ', 'ВГЕ', 'ГДЕА', 'ДЖ', 'ЕЖИ', 'ЖГЗК', 'ЗБД', 'ИКЖ', 'КЗ']
s = ['АВ', 'БГА', 'ВГЕ', 'ГЕД', 'ДЖ', 'ЕЖИ', 'ЖГЗК', 'ЗБД', 'ИКЖ', 'КЗ']
d = {i[0]: i[1:] for i in s}
start = 'Ж'
ways = {start}
c = set()
while ways:
    ways = {i + j for i in ways for j in d[i[-1]]}
    c |= {i for i in ways if i[0] == i[-1] == start}
    ways = ways.difference(c)
    # print(ways)
    ways = {w for w in ways if all(w.count(j) == 1 for j in w)}
    # print(ways)
    # input()
print(len(c))

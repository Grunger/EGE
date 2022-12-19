import sys
from time import time

# чтение потокового ввода
# в результате - двумерный список
data = sys.stdin.readlines()
for i in range(len(data)):
    data[i] = [int(j) for j in data[i].split()]
# bfs
n = len(data)  # размеры поля
s = [(data[0][0], 0, 0, [(0, 0)])]  # всевозможные текущие позиции (требуемая энергия, y, x)
ans = set()  # конечные запасы энергии
stock = 710  # начальный запас
start = time()  # время начала программы
while s:  # пока есть нерассмотренные позиции
    curr = s.pop()  # берем одну из позиций
    if stock - curr[0] <= 0:  # если энергии требуется больше, чем начальный запас, то такую позицию забываем
        continue
    if curr[1] == curr[2] == n - 1: # если дошли до конечной точки, то добавляем в ответ
        ans.add(curr[0])
        print(curr)
        continue
    if curr[1] == n - 1:  # если позиция в первом столбце, движемся только вниз
        s.append((curr[0] + data[curr[1]][curr[2] + 1], curr[1], curr[2] + 1, curr[3] + [(curr[1], curr[2] + 1)]))
    elif curr[2] == n - 1:  # если позиция в первой строке, движемся только влево
        s.append((curr[0] + data[curr[1] + 1][curr[2]], curr[1] + 1, curr[2], curr[3] + [(curr[1] + 1, curr[2])]))
    else:
        s.append((curr[0] + data[curr[1]][curr[2] + 1], curr[1], curr[2] + 1, curr[3] + [(curr[1], curr[2] + 1)]))
        s.append((curr[0] + data[curr[1] + 1][curr[2]], curr[1] + 1, curr[2], curr[3] + [(curr[1] + 1, curr[2])]))
print(sorted(ans))
print(stock - min(ans))
print(stock - max(ans))
print(f'Time: {time() - start}')

def divs(x):
    """Функция поиска делителей числа
    :return Множество из делителей"""
    d = set()
    for i in range(2, x):
        if x % i == 0:
            d.add(i)
    return d


for m in range(1000):
    s = '>' + '1' * 10 + '2' * 20 + '3' * m  # начальная строка
    # алгоритм из задания
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>3' in s:
            s = s.replace('>3', '1>', 1)
    s = s.replace('>', '')  # убираем символ >
    s = sum(int(i) for i in s)  # сумма цифр строки
    d = divs(s)  # получаем все делители
    if len(d) == 5:  # количество делителей
        print(m, d)
        break

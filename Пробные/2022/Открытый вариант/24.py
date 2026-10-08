with open('107_24.txt') as f:
    k = 0  # Текущее количество
    m = 0  # Максимум
    s = f.readline().strip()
    # Идея: подряд идущие пары начинаются либо с четной
    # либо с нечетной позиции.
    for start in range(2):
        for i in range(start, len(s), 2):
            if s[i:i+2] in {'AB', 'CB'}:
                k += 1
            else:
                m = max(m, k)
                k = 0
    print(m)

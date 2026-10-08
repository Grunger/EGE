with open('24.txt') as f:
    k = 0
    m = 0
    s = f.readline().strip()
    for start in range(2):
        for i in range(start, len(s), 2):
            if s[i:i+2] in {'AB', 'AC', 'AD'}:
                k += 1
            else:
                m = max(m, k)
                k = 0
    print(m)

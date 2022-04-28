with open('24.txt') as f:
    k = 0
    m = 0
    s = f.readline().strip()
    for i in range(1, len(s) - 2, 3):
        if s[i] == s[i + 1] and s[i + 1] == s[i + 2]:
            k += 1
        else:
            m = max(m, k)
            k = 0
    print(m)
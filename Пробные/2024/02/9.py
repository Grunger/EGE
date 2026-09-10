with open('9.csv') as f:
    k = 0
    for line in f:
        a = [int(i) for i in line.split(';')]
        count = [a.count(i) for i in a]
        if count.count(3) == 6:
            repeat = [i for i in a if a.count(i) > 1]
            single = [i for i in a if a.count(i) == 1]
            if (max(repeat) + min(repeat)) / 2 < single[0]:
                k += 1
    print(k)

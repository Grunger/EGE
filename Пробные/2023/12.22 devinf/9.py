with open('9.csv') as f:
    k = 0
    s = f.readlines()
    for line in s:
        line = [int(i) for i in line.split(';')]
        line.sort()
        if (line[0] + line[-1]) ** 2 > line[1] ** 2 + line[2] ** 2 + line[3] ** 2 + line[4] ** 2:
            k += 1
        elif [line.count(i) for i in line].count(3) == 3 and\
                [line.count(i) for i in line].count(1) == 3:
            k += 1
    print(k)

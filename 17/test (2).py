with open('17.txt') as f:
    data = [int(i) for i in f.readlines()]
    m = max(i for i in data if len(str(i)) > 1 and str(i)[-1] == str(i)[-2])
    sums = [data[i] + data[i + 1] for i in range(len(data) - 1) if
            (data[i] % 5 == 0 or data[i] % 7 == 0 or data[i + 1] % 5 == 0 or data[i + 1] % 7 == 0) and data[i] + data[
                i + 1] <= m]
    print(m)
    print(len(sums), max(sums))

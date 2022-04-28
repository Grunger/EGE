with open('17.txt') as f:
    data = map(int, f.readlines())
    data = [x for x in data if x % 19 == 6 and (x % 5 == 0 and x % 11 != 0 or x % 11 == 0 and x % 5 != 0)]
    print(len(data))
    print(max(data))



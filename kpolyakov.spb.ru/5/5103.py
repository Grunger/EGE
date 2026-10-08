result = set()
for i in range(10000):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = '1' + n + '10'
    else:
        n = '11' + n + '0'
    result.add(int(n, 2))
print(len([i for i in result if 800 <= i <= 1500]))

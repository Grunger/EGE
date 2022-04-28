b = 19
for i in range(10):
    for j in range(10):
        n = f'390{i}{j}451'
        if int(n) % b == 0:
            print(n, int(n) // b)
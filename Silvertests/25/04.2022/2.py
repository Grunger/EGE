b = 27
for i in range(10):
    for j in range(10):
        n = f'346{i}456{j}'
        if int(n) % b == 0:
            print(n, int(n) // b)
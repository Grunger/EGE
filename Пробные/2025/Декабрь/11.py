from math import ceil, log

for N in range(1, 10000):
    i = ceil(log(N, 2))
    I = ceil(i * 50 / 8)
    I = I * 1345777 / 1024 / 1024
    if I > 23:
        print(N)
        break
    
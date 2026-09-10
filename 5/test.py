k = 0
for n in range(1000):
    n_ = n
    n = bin(n)[2:]
    if n[-1] == '1':
        n = '1' + n + '00'
    else:
        n += bin(sum(int(i) for i in n))[2:]
    if 500 <= int(n, 2) <= 700:
        k += 1
        print(n_)
print(f'{k=}')

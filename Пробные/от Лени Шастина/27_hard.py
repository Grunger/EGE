f = open('270.txt')
n, k, d = map(int, f.readline().split())

data = list(map(int, f.readlines()))
all_sum = sum(data)

# остаток: сумма, длина
s = 0
total_sum = 0
tail_sum = [0] + [None] * (k - 1)
tail_len = [0] * k
for i in range(n):
    total_sum += data[i]

    ost = total_sum % k
    if tail_sum[ost] is not None:
        # хвост уже есть
        sm = total_sum - tail_sum[ost]
        if (all_sum - sm) % d == 0 and sm > s and (n - tail_len[ost] - i) % 2 == 1:
            s = sm
    else:
        tail_sum[ost] = total_sum
        tail_len[ost] = i

    print(data[i])
    print(total_sum)
    print(tail_sum)
    print(tail_len)
    print(f'{s=}', '\n')

print(s)

# 28
# 502502
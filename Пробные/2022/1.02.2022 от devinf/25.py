def divs1(x):
    d = []
    for k in range(2, x // 2 + 1):
        if len(d) > 2:
            break
        if x % k == 0:
            d.append(k)
    return sorted(d)


def divs(x):
    d = set()
    k = 2
    while k ** 2 <= x:
        if x % k == 0:
            d.add(k)
            d.add(x // k)
        k += 1
    return sorted(d)


# k = 0
# x = 1_200_000
# while k < 5:
#     d = divs(x)
#     if x % 100000 == 0:
#         print(x)
#     # print(x, d, sum(d[:3]))
#     if len(d) >= 4 and sum(d[:4]) % 2022 == 0:
#         print(x, sum(d[:4]))
#         k += 1
#     x -= 1

k = 0
x = 1_200_000
while k < 5:
    d = divs(x)
    d = [i for i in d if i <= x / 2][-3:]
    if len(d) == 3 and sum(d) % 2022 == 0 and sum(d) != x:
        print(x, sum(d))
        k += 1
    x -= 1

# for i in range(50):
#     print(i, divs(i))

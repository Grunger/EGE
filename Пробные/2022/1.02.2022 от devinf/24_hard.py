# d = dict()
# with open('24_8.txt') as f:
#     for x in f.read():
#         d[x] = d.get(x, 0) + 1
#
# for x in sorted(d.values(), reverse=True):
#     for i in d:
#         if d[i] == x:
#             print(i, x)

k = 0
with open('24.txt') as f:
    data = [i for i in f.read().strip()]
    for i in range(1, len(data)):
        if data[i] in 'DEV' and data[i + 1] in 'INF' or data[i] in 'DEV' and data[i - 1] in 'INF':
            k += 1
    print(k)



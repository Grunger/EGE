def f(s):
    return [s + 2, s + 3, s * 2]


n = [10]
for i in range(5):
    n = [x for j in n for x in f(j)]
print(len(set(n)))

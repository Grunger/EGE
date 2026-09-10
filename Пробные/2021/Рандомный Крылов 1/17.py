a = []
for i in range(2244, 7722 + 1):
    if i % 2 and i % 17 == 0 and i % 45 > 40:
        a.append(i)
print(a)
print(len(a), sum(a))

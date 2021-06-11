a = []
for i in range(1206, 14993):
    if i % 10 in (3, 6) and all(i % x != 0 for x in (3, 4, 5)):
        a.append(i)
print(len(a), min(a))

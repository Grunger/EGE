def move(h):
    a, b = h
    return (a + 1, b), (a * 3, b), (a, b + 1), (a, b * 3)


win = 99
first = 8
table = {(k, s): 0 for k in range(500) for s in range(500)}
for k in table:
    if any(sum(t) >= win for t in move(k)):
        table[k] = 1
# 19
for k in table:
    if table[k] == 0 and any(table[t] == 1 for t in move(k)):
        table[k] = -1
print('19:', min(i for i in range(91) if table[(first, i)] == -1))
# 20
# clean
for k in table:
    if table[k] == -1:
        table[k] = 0
for k in table:
    if table[k] == 0 and all(table[t] == 1 for t in move(k)):
        table[k] = -1
for k in table:
    if table[k] == 0 and any(table[t] == -1 for t in move(k)):
        table[k] = 2
print('20:', len([i for i in range(91) if table[(first, i)] == 2]))
# 21
print('21:', max(i for i in range(91) if table[(first, i)] == -1))
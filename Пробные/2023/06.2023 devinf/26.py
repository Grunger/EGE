f = open('26_T.txt')
k = int(f.readline())
n = int(f.readline())
a = [[int(j) for j in i.split()] for i in f]
a.sort()
q = []
oper = [0] * k
last = 0
count = 0
for t in range(86400):
    # освобождение
    for i in range(k):
        if oper[i] == t:
            oper[i] = 0
    # уходят из очереди
    while t in q:
        q.remove(t)
    # прием из очереди
    while 0 in oper and q:
        last = oper.index(0)
        count += 1
        oper[oper.index(0)] = q.pop(0)
    # занимаем
    for st, fn in a:
        if st == t:
            # есть пришедший
            if 0 in oper:
                # принимают сразу
                last = oper.index(0)
                count += 1
                oper[oper.index(0)] = fn
            else:
                # встает в очередь
                q.append(fn)
print(count, last + 1)

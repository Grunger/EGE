f = open('demo_23.txt').read().strip().split('\n')
g = []
for line in f:
    l, m, w = line.split()
    g.append([int(l), int(m), float(w)])

# кратчайший путь
weight = [0, 0] + [float('inf')] * 10000
for i in range(len(g)):
    for l, m, w in g:
        weight[m] = min(weight[m], weight[l] + w)
print(weight[100])

# самый длинный путь
weight = [0, 0] + [float('-inf')] * 10000
for i in range(len(g)):
    for l, m, w in g:
        weight[m] = max(weight[m], weight[l] + w)
print(weight[100])

# количество путей
# нужна топологическая сортировка -> сложно


import sys

data = sys.stdin.read().strip().split('\n')

for i, a in enumerate(data):
    data[i] = a.split('\t')
time = {'0': 0}
deps = {'0': ()}
for id, t, d in data:
    time[id] = int(t)
    deps[id] = tuple(d.split('; '))
print(time)
print(deps)
for id, t, d in data:
    m = max(time[i] for i in deps[id])
    time[id] += m
print(time)
print(max(time.values()))

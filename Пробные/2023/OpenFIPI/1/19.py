def move(x):
    return x + 1, x + 3, x * 2

pos = [0] * 1000
for i in range(1000):
    if i >= 443:
        pos[i] = 5

for i in range(500):
    if pos[i] == 0 and any(pos[x] == 5 for x in move(i)):
        pos[i] = 1
for i in range(500):
    if pos[i] == 0 and all(pos[x] == 1 for x in move(i)):
        pos[i] = -1
for i in range(500):
    if pos[i] == 0 and any(pos[x] == -1 for x in move(i)):
        pos[i] = 2

for i in range(500):
    if pos[i] == 0 and all(pos[x] > 0 for x in move(i)):
        pos[i] = -2

for i in range(500):
    if pos[i] == -2:
        print(i)

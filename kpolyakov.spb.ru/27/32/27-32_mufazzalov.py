# Автор: Д. Муфаззалов

f = open('27-32b.txt')
s = [0]
for _ in range(int(f.readline())):
    nums = list(map(int, f.readline().split()))
    t=[x + i for x in s for i in nums]
    s = {(x % 11): x for x in sorted(t, reverse=True)}.values()
print(*[x for x in s if x % 11 == 0])

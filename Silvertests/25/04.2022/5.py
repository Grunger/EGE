# 745*356*2
# 100000000 8

b = 77
ans = set()
n = int(f'7453562')
if n % b == 0:
    ans.add((n, n // b))
for i in range(100):
    n = int(f'745{i}3562')
    if n % b == 0:
        ans.add((n, n // b))
    n = int(f'745356{i}2')
    if n % b == 0:
        ans.add((n, n // b))
    i = str(i).rjust(2, '0')
    n = int(f'745{i}3562')
    if n % b == 0:
        ans.add((n, n // b))
    n = int(f'745356{i}2')
    if n % b == 0:
        ans.add((n, n // b))
for i in range(10):
    for j in range(10):
        n = int(f'745{i}356{j}2')
        if n % b == 0:
            ans.add((n, n // b))

for i in sorted(ans):
    print(*i)

# 74535692 967996
# 745135622 9677086
# 745356612 9679956
# 745383562 9680306
# 745935652 9687476


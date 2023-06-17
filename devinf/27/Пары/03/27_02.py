# максимальное произведение, кратное 22

def slow():
    mx = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (a[i] * a[j]) % 22 == 0:
                mx = max(mx, a[i] * a[j])
    return mx


def fast():
    mx22 = 0
    mx11 = 0
    mx2 = 0
    mx = 0
    for x in a:
        if x % 22 == 0:
            mx22 = max(x, mx22)
        elif x % 11 == 0:
            mx11 = max(x, mx11)
        elif x % 2 == 0:
            mx2 = max(x, mx2)
        mx = max(x, mx)
    return max(mx22 * mx, mx2 * mx11)


f = open('27_B.txt')
n = int(f.readline())
a = [int(i) for i in f]
print(fast())


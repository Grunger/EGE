# 7^500 + 7^200 – 7^50 – Х

def f(x):
    n = 7**500 + 7**200 - 7**50 - x
    s = ''
    while n:
        s += str(n % 7)
        n //= 7
    return sum(int(i) for i in s)


a = []
for j in range(100):
    a.append(f(7**200 + j - 50))
print(max(a))

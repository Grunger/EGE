from functools import lru_cache

def m(x):
    return x - 2, x - 4, x // 3

@lru_cache(None)
def g(s):
    if s <= 10:
        return 5
    if any(g(i) == 5 for i in m(s)):
        return 1
    if all(g(i) == 1 for i in m(s)):
        return -1    
    if any(g(i) == -1 for i in m(s)):
        return 2
    if all(g(i) > 0 for i in m(s)):
        return -2
    return 0

print(19)
for s in range(11, 300):
    if g(s) == -1:
        print(s)
print('-' * 10)
print(20)
for s in range(11, 300):
    if g(s) == 2:
        print(s)
print('-' * 10)
print(21)
for s in range(11, 300):
    if g(s) == -2:
        print(s)
from functools import lru_cache


@lru_cache(None)
def f(s, e):
    print(s, e)
    if s > e:
        return 0
    if s == e:
        return 1
    if s % 10 == 0 or s % 10 == 1:
        return f(s + 5, e) + f(s + 10, e)
    return f(s + 5, e) + f(s + 10, e) + f(s * (s % 10), e)


print(f(10, 220))

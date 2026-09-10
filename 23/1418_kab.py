# 5 -> 280, v30 x60
# +5 *5

def f(start, end, skip=0):
    if start > end:
        return 0
    if start == skip:
        return 0
    if start == end:
        return 1
    return f(start + 5, end, skip) + f(start * 5, end, skip)


print(f(5, 30) * f(30, 280, 60))

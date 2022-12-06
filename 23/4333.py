def f(start, end, program):
    if '11' in program or '22' in program or '33' in program or start == 6:
        return 0
    if start > end:
        return 0
    if start == end:
        return 1
    return f(start + 1, end, program + '1') + f(start + 3, end, program + '2') + f(start**2, end, program + '3')

print(f(1, 5, ''), f(5, 25, ''))

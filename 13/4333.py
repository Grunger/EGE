def f(start, end, program, nums):
    if '11' in program or '22' in program or '33' in program or start == 6:
        return 0
    if start > end:
        return 0
    if start == end and 5 in nums:
        print(nums)
        return 1
    return f(start + 1, end, program + '1', nums + [start + 1]) +\
           f(start + 3, end, program + '2', nums + [start + 3]) + \
           f(start**2, end, program + '3', nums + [start ** 2])

print(f(1, 25, '', []))

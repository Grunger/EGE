from fnmatch import fnmatch


# for i in range(10**7, 10**10):
#     if i % 2023 == 0 and fnmatch(str(i), '1?2139*4'):
#         print(i, i // 2023)
# 162139404

for i in range(0, 10**10, 2023):
    if fnmatch(str(i), '1?2139*4'):
        print(i, i // 2023)

from random import choice


# s = 'QWERTYUIOPASDFGHJKLZXCVBNM'
# with open('24.txt', 'w') as f:
#     for _ in range(20222022):
#         f.write(choice(s))

data = open('24.txt').read().replace('I', 'G', 5034)
with open('24.txt', 'w') as f:
    f.write(data)

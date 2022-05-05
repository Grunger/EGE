from string import ascii_uppercase

d = {i: 0 for i in ascii_uppercase}
for i in open('24-157.txt').read().strip():
    d[i] += 1
print(d)
print(len([i for i in d if d[i] % 2 == 1]))
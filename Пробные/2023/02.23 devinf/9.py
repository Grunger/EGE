import csv
from itertools import permutations



reader = csv.reader(open('9.csv'), delimiter=';')
k = 0
for line in reader:
    line = [int(i) for i in line]
    twice = len([i for i in line if line.count(i) == 2])
    once = len([i for i in line if line.count(i) == 1])
    if twice == 2 and once == 4 and any(sum(j[:3]) == sum(j[3:]) for j in permutations(line)):
        k += 1
        print(line)
print(k)

import csv

reader = csv.reader(open('9.csv'), delimiter=';')
k = 0
for line in reader:
    line = [int(i) for i in line]
    single = [i for i in line if line.count(i) == 1]
    twice = [i for i in line if line.count(i) == 2]
    if twice and all(i > j for i in twice for j in single):
        print(line)
        k += 1
print(k)

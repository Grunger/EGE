import csv

reader = csv.reader(open('9.csv'), delimiter=';')
k = 0
for line in reader:
    line = [int(i) for i in line]
    repeat = [i for i in line if line.count(i) > 1]
    single = [i for i in line if line.count(i) == 1]
    if any(repeat.count(i) == 2 for i in repeat) and all(i > j for i in repeat for j in single):
        print(line)
        k += 1
print(k)

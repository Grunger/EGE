import csv

reader = csv.reader(open('9.csv'), delimiter=';')
k = 0
for line in reader:
    line = [int(i) for i in line]
    double = {i for i in line if line.count(i) > 1}
    single = [i for i in line if line.count(i) == 1]
    if len(double) == 0 and sum(single) / len(single) >= (sorted(single)[2] + sorted(single)[3]) / 2:
        k += 1
print(k)

import csv

reader = csv.reader(open('9.csv'), delimiter=';')
k = 0
for line in reader:
    line = [int(i) for i in line]
    double = [i for i in line if line.count(i) > 1]
    single = [i for i in line if line.count(i) == 1]
    p = 1
    for i in double:
        p *= i
    if len(single) == 2 and single[0] * single[1] <= p ** (1 / len(double)):
        k += 1
print(k)

f = open('10 Собачье сердце.txt', encoding='cp1251')
data = f.read().split()

k1 = []

for i in range(len(data)):
    st1 = data[i].lower()
    if 'в' in st1 and 'а' not in st1 and 'о' not in st1:
        k1.append(st1)
k2 = []
with open('10 Собачье сердце 2.txt') as f2:
    data2 = []
    while s := f2.readline():
        data2.extend(s.split())
    for i in range(len(data2)):
        st1 = data[i].lower()
        print(st1)
        if 'в' in st1 and 'а' not in st1 and 'о' not in st1:
            k2.append(st1)
print(len(k1), len(k2))
print(k1[-5:])
print(k2[-5:])

f = open('10 Собачье сердце.txt', encoding='cp1251')
data = f.read().split()
k = 0
for i in data:
    i = i.lower()
    print(i)
    if 'в' in i and 'а' not in i and 'о' not in i:
        k += 1
print(k)

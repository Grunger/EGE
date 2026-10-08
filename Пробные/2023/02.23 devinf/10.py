f = open('10.txt').read()
k = 0
for word in f.split():
    if 'род' in word.lower() and len(word) > 3:
        k += 1

print(k)

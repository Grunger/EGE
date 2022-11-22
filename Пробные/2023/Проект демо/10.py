text = open('10.txt', encoding='cp1251').read()
print(text.count('теперь'))

for word in text.split():
    if 'теперь' in word:
        print(word)

text = open('107_10.txt').read()
for line in text.split():
    if 'душа' in line:
        print(line)

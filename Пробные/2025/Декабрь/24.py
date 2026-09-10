s = open('24.txt','r').read().strip()
s = s.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
s = s.split('1')
print(len(max([i for i in s if i.count('Q') == 35], key = len)) + 2)

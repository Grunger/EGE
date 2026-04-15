from re import *

s = open('2AB916.txt').read()
r = '([A][B][ABCDEF]*){2}'
for i in finditer(r, s):
    res = i.group()
    print(res)
    break

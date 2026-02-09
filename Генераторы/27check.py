from turtle import *

tracer(0)
pu()
m = 30
edges = [(1, 4, 2, 5), (4, 7, 7, 10)]
with open('27A.txt') as f:
    s = f.read().strip().replace(',', '.').split('\n')

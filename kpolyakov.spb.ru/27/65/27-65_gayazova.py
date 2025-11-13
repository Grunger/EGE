# Автор: Н. Гаязова

f=open("27-64a.txt","r")
N = int(f.readline())
D = [[20000] * 2 for i in range(2)]
sm=0
sb=0
for i in range(N):
    a, b = map(int, f.readline().split())
    if a % 2 == 1:
        if a > b: a, b = b, a
        D[a % 2][b % 2]=min(a+b,D[a % 2][b % 2])
        sm+=a
        sb+=b
if sm%2==0 and sb%2==1: print(sm+sb)
else: print(sm+sb-D[sm%2][1-sb%2])
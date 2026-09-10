# Автор: А.Н. Носкин

F = open("27-52b.txt")
N = int(F.readline())# кол-во строк
a = [] #массив с остатками 0
b = [] #массив с остатками 1
c = [] #массив с остатками 2
for i in range(N):
  x = int(F.readline())
  if x%3 == 0:
    a.append(x)
  elif x%3 == 1:
    b.append(x)
  elif x%3 == 2:
    c.append(x)
a.sort(reverse = True)
b.sort(reverse = True)
c.sort(reverse = True)
summ0 = sum(a[:3])# сумма первых 3х с ост 0
summ1 = sum(b[:3])# сумма первых 3х с ост 1
summ2 = sum(c[:3])# сумма первых 3х с ост 2
summ012 = a[0]+b[0]+c[0] # сумма ост 0+1+2
Max = max(summ0,summ1,summ2,summ012)
print(Max)
 

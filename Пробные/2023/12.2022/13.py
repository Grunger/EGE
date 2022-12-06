w = ['АБДЕ',
     'БВЗ',
     'ВЖЗ',
     'ГАБ',
     'ДИ',
     'ЕДЗ',
     'ЖЗЛ',
     'ЗГЛ',
     'ИЕЗК',
     'КЗ',
     'ЛК']
w = {i[0]: i[1:] for i in w}
k = 0
ways = {'З'}
ways = {i + j for i in ways for j in w[i]}
while ways:
    print('all', ways)
    print('end', {i for i in ways if i[-1] == 'З'})
    print('---')
    k += len({i for i in ways if i[-1] == 'З'})
    ways = {i for i in ways if i[-1] != 'З'}
    ways = {i + j for i in ways for j in w[i[-1]] if j not in i or j == 'З'}
print(k)

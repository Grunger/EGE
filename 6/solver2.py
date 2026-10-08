s = '''Повтори 3 [Вперёд 32 Направо 90 Вперёд 38 Направо 90]
Поднять хвост
Вперёд 25 Направо 90 Вперёд 21 Налево 90
Опустить хвост
Повтори 3 [Вперёд 29 Направо 90 Назад 18 Направо 90]'''.split('\n')

dir = '0'

# первая фигура
commands = s[0].split()
rep = int(s[1])
com1 = ''.join(i for i in s[2] if i.isalpha())
move1 = int(s[3])
com2 = ''.join(i for i in s[4] if i.isalpha())
move2 = int(s[5])
com3 = ''.join(i for i in s[6] if i.isalpha())
move3 = int(s[7])
com4 = ''.join(i for i in s[8] if i.isalpha())
move4 = int(s[9])

from random import randint, random, gauss

def gent():
    with open('27-T.txt', 'w') as f:
        dots = set()
        while len(dots) < 100:
            x, y = randint(-2, 0) + random(), randint(-2, 0) + random()
            x = round(x, 16)
            y = round(y, 16)
            while not(x > -1 and x < -0.5 and y > -1 and y < -0.5):
                x, y = randint(-2, 0) + random(), randint(-2, 0) + random()
                x = round(x, 16)
                y = round(y, 16)            
            dots.add((x, y))
        while len(dots) < 200:
            x, y = randint(0, 2) + random(), randint(0, 2) + random()
            x = round(x, 16)
            y = round(y, 16)
            while not(x > 1 and x < 1.5 and y > 1 and y < 1.5):
                x, y = randint(0, 2) + random(), randint(0, 2) + random()
                x = round(x, 16)
                y = round(y, 16)            
            dots.add((x, y)) 
        while len(dots) < 250:
            x, y = randint(-2, 1) + random(), randint(-2, 1) + random()
            x = round(x, 16)
            y = round(y, 16)          
            dots.add((x, y))     
        for d in dots:
            f.write(f'{d[0]}\t{d[1]}\n'.replace('.', ','))


def gena():
    with open('27-A.txt', 'w') as f:
        dots = set()
        print('cl1')
        while len(dots) < randint(350, 450):
            x, y = randint(-2, 0) + random(), randint(-3, 0) + random()
            x = round(x, 16)
            y = round(y, 16)
            while not(y < x and y > x ** 2 - 3 and x < 0):
                x, y = randint(-2, 0) + random(), randint(-3, 0) + random()
                x = round(x, 16)
                y = round(y, 16)            
            dots.add((x, y))
        print('cl2')
        while len(dots) < randint(750, 850):
            x, y = randint(0, 2) + random(), randint(0, 3) + random()
            x = round(x, 16)
            y = round(y, 16)
            while not(y < x and y > x ** 2 - 3 and y > 0):
                x, y = randint(0, 2) + random(), randint(0, 3) + random()
                x = round(x, 16)
                y = round(y, 16)            
            dots.add((x, y))
        print('other')
        d = len(dots)
        while len(dots) < d + 10:
            x, y = randint(-3, 3) + random(), randint(-3, 3) + random()
            x = round(x, 16)
            y = round(y, 16)          
            dots.add((x, y))     
        for d in dots:
            f.write(f'{d[0]}\t{d[1]}\n'.replace('.', ','))
            
def genb():
    with open('27-Б.txt', 'w') as f:
        dots = set()
        # 1 кластер
        print(1)
        while len(dots) < 2000:
            x, y = randint(-2, 1) + random(), randint(0, 1) + random()
            x = round(x, 16)
            y = round(y, 16)
            while not(y > x + 2 and x**2 + y**2 < 4):
                x, y = randint(-2, 1) + random(), randint(0, 1) + random()
                x = round(x, 16)
                y = round(y, 16)            
            dots.add((x, y))
        # 2 кластер
        print(2)
        while len(dots) < 4000:
            x, y = 1 + random(), randint(-2, 1) + random()
            x = round(x, 16)
            y = round(y, 16)
            while not(x**2 + y ** 2 < 4 and x > 1):
                x, y = 1 + random(), randint(-2, 1) + random()
                x = round(x, 16)
                y = round(y, 16)            
            dots.add((x, y))
        # 3 кластер
        print(3)
        while len(dots) < 6000:
            x, y = randint(-5, -1) + random(), randint(-3, -1)+ random()
            x = round(x, 16)
            y = round(y, 16)
            while not(x**2 + y ** 2 > 4 and y < x + 2 and y > -3):
                x, y = randint(-5, -1) + random(), randint(-3, -1)+ random()
                x = round(x, 16)
                y = round(y, 16)            
            dots.add((x, y))
        # аномалии
        print(5)
        while len(dots) < 7_000:
            x, y = randint(-5, 2) + random(), randint(-4, 3) + random()
            x = round(x, 16)
            y = round(y, 16)          
            dots.add((x, y))     
        for d in dots:
            f.write(f'{d[0]}\t{d[1]}\n'.replace('.', ','))
            

genb()
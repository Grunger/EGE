from turtle import *

left(90)
color('black', 'red')
begin_fill()
for i in range(3):
    forward(100)
    right(120)

end_fill()
canvas = getcanvas()
k = 0
for y in range(-1000, 1000, 10):
    for x in range(-1000, 1000, 10):
        item = canvas.find_overlapping(x, y, x, y)
        if item:
            print(x, y, item)
            colors = [canvas.itemcget(i, "fill") for i in item]
            if 'red' in colors and 'black' not in colors:
                k += 1
print(k)
done()

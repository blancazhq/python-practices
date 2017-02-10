from turtle import *

def draw_triangle(size, fill, color):
    if fill is True:
        begin_fill()

    for i in range(3):
        left(120)
        fd(size)
    if fill == True:
        fillcolor(color)

    if fill is True:
        end_fill()



def draw_square(size, fill, color):
    if fill is True:
        begin_fill()

    for i in range(4):
        left(90)
        fd(size)
    if fill == True:
        fillcolor(color)

    if fill is True:
        end_fill()


def draw_pentagon(size, fill, color):
    if fill is True:
        begin_fill()

    left(54)
    fd(size)
    for i in range(4):
        right(72)
        fd(size)
    if fill == True:
        fillcolor(color)

    if fill is True:
        end_fill()



def draw_hexagon(size, fill, color):
    if fill is True:
        begin_fill()

    left(60)
    fd(size)
    for i in range(5):
        right(60)
        fd(size)
    if fill == True:
        fillcolor(color)

    if fill is True:
        end_fill()




def draw_octagon(size, fill, color):
    if fill is True:
        begin_fill()
    left(67.5)
    fd(size)
    for i in range(7):
        right(45)
        fd(size)
    if fill == True:
        fillcolor(color)


    if fill is True:
        end_fill()



def draw_star(size, fill, color):
    if fill is True:
        begin_fill()
    left(18)
    fd(size)
    for i in range(4):
        left(144)
        fd(size)
    if fill == True:
        fillcolor(color)


    if fill is True:
        end_fill()



def draw_circle(size, fill, color):
    if fill is True:
        begin_fill()
    n = 45
    a = ((n-2) * 180)/n

    left(a/2)
    fd(size)
    for i in range(n-1):
        right(180-a)
        fd(size)

    if fill == True:
        fillcolor(color)


    if fill is True:
        end_fill()

#change happened between 45 and 50

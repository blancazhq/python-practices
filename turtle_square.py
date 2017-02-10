from turtle import *

def draw_square():
    for i in range(4):
        left(90)
        fd(120)

fillcolor("red")

begin_fill()
draw_square()
end_fill()

mainloop()

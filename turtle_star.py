from turtle import *

def draw_star():
    left(18)
    fd(120)
    for i in range(4):
        left(144)
        fd(120)


fillcolor("purple")

begin_fill()
draw_star()
end_fill()

mainloop()

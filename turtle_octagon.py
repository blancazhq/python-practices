from turtle import *

def draw_octagon():
    left(67.5)
    fd(120)
    for i in range(7):
        right(45)
        fd(120)


fillcolor("blue")

begin_fill()
draw_octagon()
end_fill()

mainloop()

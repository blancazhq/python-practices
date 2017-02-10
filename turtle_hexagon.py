from turtle import *

def draw_hexagon():
    left(60)
    fd(120)
    for i in range(5):
        right(60)
        fd(120)


fillcolor("blue")

begin_fill()
draw_hexagon()
end_fill()

mainloop()

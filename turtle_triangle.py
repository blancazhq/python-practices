from turtle import *

def draw_triangle():
    for i in range(3):
        left(120)
        fd(120)

fillcolor("orange")

begin_fill()
draw_triangle()
end_fill()

mainloop()

from turtle import *

def draw_circle():
    n = 45
    a = ((n-2) * 180)/n

    left(a/2)
    fd(5)
    for i in range(n-1):
        right(180-a)
        fd(5)

#change happened between 45 and 50

fillcolor("blue")

begin_fill()
draw_circle()
end_fill()

mainloop()

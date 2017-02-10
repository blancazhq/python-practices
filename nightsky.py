from shapes import *
import random

bgcolor("black")

for i in range(12):
    m = random.choice(range(150))
    draw_star(m, True, "yellow")
    n = random.choice(range(300))

    up()
    fd(n)
    down()

mainloop()

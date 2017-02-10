import matplotlib.pyplot as plot
import numpy as np

def f(n):
    if n % 2 == 1:
        return 1
    else:
        return -1

x = range(-5, 6)

result = []

for n in x:
    result.append(f(n))

plot.bar(x, result)

plot.show()

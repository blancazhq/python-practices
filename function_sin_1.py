import matplotlib.pyplot as plot
import numpy as np

def f(n):
    return np.sin(n)

x = range(-6, 6)

sin_result = []

for n in x:
    sin_result.append(f(n))

plot.plot(x, sin_result)

plot.show()

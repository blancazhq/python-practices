import matplotlib.pyplot as plot
import math
import numpy as np

def f(n):
    return n*n

x = np.linspace(-100, 100, 256, endpoint=True)

square_result = np.square(x)

plot.plot(x, square_result)

plot.show()

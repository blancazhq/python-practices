import matplotlib.pyplot as plot
import numpy as np

def f(n):
    return n * 1.8 +32

x = np.linspace(-50, 50, 200, endpoint=True)

plot.plot(x, f(x))

plot.show()

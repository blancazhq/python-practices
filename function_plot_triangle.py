import matplotlib.pyplot as plot
import numpy as np

def f(n):
    if n == 2:
        return 1
    elif n == 3:
        return 6
    elif n ==4:
        return 1

x = np.array[2, 3, 4]

"""
result = []

for n in x:
    result.append(f(n))
"""

plot.plot(x, f(n))

#plot.plot(x, result)

plot.show()

import matplotlib.pyplot as plot
import math
import numpy as np

x = np.linspace(-6, 6, 256, endpoint=True)

square_result = np.sin(x)

plot.plot(x, square_result)

plot.show()

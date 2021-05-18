######## exponential ##########


import numpy as np
import matplotlib.pyplot as plt 


x = np.arange(-5, 5, 0.1)

y  = np.exp(x)

plt.plot(x, y)
plt.xlabel("Independent Variable")
plt.ylabel("Dependent Variable")
plt.show()
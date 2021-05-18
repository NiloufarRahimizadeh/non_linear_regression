### Logarithmic ###

import numpy as np 
import matplotlib.pyplot as plt


x = np.arange(-5, 5, 0.1)

y = np.log(x)

plt.plot(x, y)
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()
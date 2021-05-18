import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-5, 5, 0.1)

y = 1*(x**3) + 1*(x**2) + 1*(x) + 3

y_noise = 20 * np.random.normal(size=x.size)

y_data = y + y_noise

plt.plot(x, y_data, 'ro')

plt.plot(x, y, 'b')

plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')

plt.show()
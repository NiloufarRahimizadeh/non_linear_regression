import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5.0, 5.0, 0.1)
y = 2*(x) +3

y_noise = 2 * np.random.normal(size=x.size)
y_data = y + y_noise
plt.plot(x, y_data, 'bo')
# plt.scatter(x, y_data)
plt.plot(x,y, 'r')
plt.ylabel('Dependent Variable') 
plt.xlabel('Indepdendent Variable')
plt.show()

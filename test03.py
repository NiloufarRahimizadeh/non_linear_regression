#As you can see, this function has 𝑥3 and 𝑥2 as independent variables. 
# Also, the graphic of this function is not a straight line over the 2D plane. 
# So this is a non-linear function.


######### Quadratic #######
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-5, 5, 0.1)

y = np.power(x,2)

y_noise = 2 * np.random.normal(size=x.size)

y_data = y + y_noise

plt.plot(x, y_data, 'bo')
plt.plot(x, y)
plt.xlabel ("Independent variable")
plt.ylabel ("Dependent variable")
plt.show()
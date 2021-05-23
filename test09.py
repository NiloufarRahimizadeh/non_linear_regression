import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from scipy.optimize import curve_fit


df = pd.read_csv("china_gdp.csv")
df.head(10)

x_data, y_data = (df["Year"].values, df["Value"].values)

def sigmoid(x, Beta_1, Beta_2):
     y = 1 / (1 + np.exp(-Beta_1*(x-Beta_2)))
     return y



# Lets normalize our data
xdata =x_data/max(x_data)
ydata =y_data/max(y_data)
#plot initial prediction against datapoints

popt, pcov = curve_fit(sigmoid, xdata, ydata)
#print the final parameters
print(" beta_1 = %f, beta_2 = %f" % (popt[0], popt[1]))
x = np.linspace(1960, 2015, 55)
x = x/max(x)
plt.figure(figsize=(8,5))
y = sigmoid(x, popt[0], popt[1])
plt.plot(xdata, ydata, 'ro', label='data')
plt.plot(x,y, linewidth=3.0, label='fit')
plt.legend(loc='best')
plt.ylabel('GDP')
plt.xlabel('Year')
plt.show()
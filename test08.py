import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("china_gdp.csv")
df.head(10)





X = np.arange(-5.0, 5.0, 0.1)
Y = 1.0 / (1.0 + np.exp(-X))

plt.plot(X,Y) 
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()
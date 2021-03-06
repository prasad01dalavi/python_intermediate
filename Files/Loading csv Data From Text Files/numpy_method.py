import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('myFile.txt', delimiter=',', unpack=True)
# Unpacking allows to directly assign the values to x, y in the form of list

plt.plot(x, y, label='Loading From File')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Loading Data using numpy')
plt.legend()
plt.show()



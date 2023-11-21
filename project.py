import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return np.sqrt(x**2) + np.sqrt(x**3) + 1.1

x = np.linspace(-0.5, 12, 1000)

y = function(x)

plt.plot(x, y, color='blue', linestyle='-', linewidth=2)

plt.title('Графік функції y = √x^2 + √x^3 + 1.1')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('grafik.png')

plt.show()

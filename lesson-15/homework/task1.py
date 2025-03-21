import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2-4*x+4

x = np.linspace(-10, 10, 10)

y = f(x)

plt.plot(x, y, label=r'f(x)=x^2-4x+4', color = 'b')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph')
plt.grid(True)
plt.show()
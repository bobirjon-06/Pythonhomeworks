import numpy as np
import matplotlib.pyplot as plt

def sin(x):
    return np.sin(x)
def cos(x):
    return np.cos(x)

x = np.linspace(0, 2*np.pi, 400)

y_sin = sin(x)
y_cos = cos(x)


plt.plot(x, y_sin, 'y--o', label=r'$\sin(x)$')

plt.plot(x, y_cos, 'g-s', label=r'$\cos(x)$')
plt.xlabel('x')
plt.ylabel('Function values')
plt.title('Plot of $\sin(x)$ and $\cos(x)$')
plt.legend()
plt.grid(True)
plt.show()
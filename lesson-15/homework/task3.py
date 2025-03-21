import numpy as np
import matplotlib.pyplot as plt

def cubic(x):
    return x**3
def sin(x):
    return np.sin(x)
def exp(x):
    return np.exp(x)
def log(x):
    return np.log(x)

x1 = np.linspace(-2, 2, 100) 
x2 = np.linspace(-2 * np.pi, 2 * np.pi, 100)
x3 = np.linspace(-2, 2, 100)
x4 = np.linspace(0, 5, 100) 

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

axs[0, 0].plot(x1, cubic(x1), 'r-', label=r'$f(x) = x^3$')
axs[0, 0].set_title('Cubic Function')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')
axs[0, 0].grid(True)
axs[0, 0].legend()

axs[0, 1].plot(x2, sin(x2), 'b--', label=r'$f(x) = \sin(x)$')
axs[0, 1].set_title('Sine Function')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('f(x)')
axs[0, 1].grid(True)
axs[0, 1].legend()

axs[1, 0].plot(x3, exp(x3), 'g-.', label=r'$f(x) = e^x$')
axs[1, 0].set_title('Exponential Function')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('f(x)')
axs[1, 0].grid(True)
axs[1, 0].legend()

axs[1, 1].plot(x4, log(x4), 'm:', label=r'$f(x) = \log(x+1)$')
axs[1, 1].set_title('Logarithm Function')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('f(x)')
axs[1, 1].grid(True)
axs[1, 1].legend()

plt.tight_layout()
plt.show()
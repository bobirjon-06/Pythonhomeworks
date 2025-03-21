import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.cos((x**2 + y**2))  

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y, indexing='xy')  
Z = f(X, Y)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='viridis')

fig.colorbar(surf, ax=ax, shrink=0.6, aspect=12)  

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('f(x, y)')
ax.set_title('3D Surface Plot of f(x, y) = cos(x² + y²)')

ax.set_box_aspect([1,1,0.7])  

plt.show()

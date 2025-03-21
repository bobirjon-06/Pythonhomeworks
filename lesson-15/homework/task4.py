import numpy as np
import matplotlib.pyplot as plt
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
colors = np.random.rand(100) 
markers = ['o', 's', '^', 'D', 'x', '*', 'p', '+, 'v', '<', '>', '|', '_']
marker_choices = np.random.choice(markers, 100)

plt.figure(figsize=(8, 6))

for i in range(100):
    plt.scatter(x[i], y[i], color=plt.cm.viridis(colors[i]), marker=marker_choices[i])

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of 100 Random Points')
plt.grid(True, linestyle='--', alpha=0.4)

plt.show()

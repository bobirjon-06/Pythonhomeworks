import numpy as np
import matplotlib.pyplot as plt

def random_data():
    return np.random.normal(0, 1, 1000)

data = random_data()

fig, ax = plt.subplots()
ax.hist(data, bins=25, alpha=0.7, color='yellow')

ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.set_title('Histogram')

plt.show()

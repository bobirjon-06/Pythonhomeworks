import numpy as np
import matplotlib.pyplot as plt

time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [5, 7, 6, 8]
category_B = [6, 5, 7, 6]
category_C = [4, 6, 5, 7]

x = range(4)  

plt.figure(figsize=(8, 5))
plt.bar(x, category_A, label='Category A', color='b')
plt.bar(x, category_B, bottom=category_A, label='Category B', color='r')
plt.bar(x, category_C, bottom=np.array(category_A) + np.array(category_B), label='Category C', color='g')

plt.xticks(time_periods) 
plt.title("Stacked Bar Chart")
plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

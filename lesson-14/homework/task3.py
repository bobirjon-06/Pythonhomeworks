import numpy as np

a = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

b = np.array([7, 4, 5])

solution = np.linalg.solve(a, b)
# print(a)
# print(b)
print(solution)
print(np.round(solution, 2))
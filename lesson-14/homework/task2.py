import numpy as np

def power(base, pow):
    return base**pow

raise_to = np.vectorize(power)
base = np.array([2, 3, 4, 5])
pow = np.array([2, 3, 4, 5])
answer = raise_to(base, pow)

print(answer)
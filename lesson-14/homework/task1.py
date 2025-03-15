import numpy as np

def conversion(f):
    return (f-32)*5/9

vec_f_to_c = np.vectorize(conversion)

temp_f = np.array([32, 68, 100, 212, 77])
temp_c = conversion(temp_f)

print(temp_c)
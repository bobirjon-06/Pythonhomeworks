#1 
import numpy as numpy   

vector = numpy.arange(10, 50)

print(vector)

#2
matrix = numpy.arange(9).reshape(3, 3)
print(matrix)

#3
id_matrix = numpy.eye(3)
print(id_matrix)

#4
rand_arr = numpy.random.random((3, 3, 3))
print(rand_arr)

#5
randArr = numpy.random.randint((10, 10))
print(randArr.min())
print(randArr.max())

#6
randVector = numpy.random.random((30))
print(randVector.mean())

#7
matrix = numpy.random.random((5, 5))
normalized_matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min())

print("\nNormalized Matrix:\n", normalized_matrix)

#8
mat1 = numpy.random.random((5,3))
mat2 = numpy.random.random((3,2))
ans = mat1 @ mat2
print(ans)

#9
mat3 = numpy.random.random((3, 3))
mat4 = numpy.random.random((3, 3))
ans = mat3 @ mat4
print(ans)

#10
matrix = numpy.random.random((4, 4))
print(  numpy.transpose(matrix))

#11
matrix = numpy.random.random((3, 3))
deter = numpy.linalg.det(matrix)
print(deter)

#12
A = numpy.random.random((3, 4))
B = numpy.random.random((4, 3))

product = numpy.dot(A, B)
print(product)

#13

A = numpy.random.random((3, 3))
B = numpy.random.random((3, 1))

matrix_vector_product = numpy.dot(A, B)
print(matrix_vector_product)

#14
x = numpy.linalg.solve(A, B)
print(x)

#15
matrix = numpy.random.random((5, 5))

row_sums = numpy.sum(matrix, axis=1)
column_sums = numpy.sum(matrix, axis=0)

print(row_sums)
print(column_sums)

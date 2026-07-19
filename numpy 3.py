import numpy as np

A = np.array([[2, 4, 6],
              [1, 3, 5],
              [7, 8, 9]])

B = np.array([[1, 0, 2],
              [3, 1, 4],
              [5, 2, 6]])

print("Matrix A")
print(A)

print("\nMatrix B")
print(B)

print("\nAddition")
print(A + B)

print("\nSubtraction")
print(A - B)

print("\nMultiplication")
print(A * B)

print("\nMatrix Product")
print(np.dot(A, B))

print("\nTranspose of A")
print(A.T)
import numpy as np

A = np.array([
    [4, 1, 0],
    [2, 3, 0],
    [0, 0, 5]
], dtype=float)

print("Matrix A:")
print(A)

eigenvalue, eigenvector = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalue)

print("\nEigenvectors:")
print(eigenvector)

P = eigenvector
print("\nMatrix P:")
print(P)

D = np.diag(eigenvalue)
print("\nMatrix D:")
print(D)

P_inv = np.linalg.inv(P)
print("\nP inverse:")
print(P_inv)

A_construct = P @ D @ P_inv
print("\nP × D × P^-1:")
print(A_construct)

A_construct = np.round(A_construct, 3)
print("\nFinal Answer:")
print(A_construct)

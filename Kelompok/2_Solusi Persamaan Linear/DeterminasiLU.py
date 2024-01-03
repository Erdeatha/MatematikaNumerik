import numpy as np

def LU_decomposition(A):
    n = len(A)
    L = np.identity(n)
    U = np.copy(A)

    for j in range(n):
        for i in range(j+1, n):
            L[i][j] = U[i][j] / U[j][j]
            U[i][j] = 0

        for i in range(j+1, n):
            for k in range(j+1, n):
                U[i][k] = U[i][k] - L[i][j] * U[j][k]

    return L, U

def solve(A, b):
    L, U = LU_decomposition(A)
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    return x

n = int(input("Masukkan ukuran matriks (n x n): "))
A = []
print(f"Masukkan elemen-elemen matriks A ({n}x{n}) (dipisahkan oleh spasi): ")
for i in range(n):
    row = [float(x) for x in input().split()]
    A.append(row)

b = [float(x) for x in input("Masukkan elemen-elemen matriks B (dipisahkan oleh spasi): ").split()]

X = solve(np.array(A), np.array(b))

print('Solusi SPL:')
for i, val in enumerate(X):
    print(f"X{i+1} = {val}")
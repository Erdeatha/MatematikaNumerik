n = int(input("Masukkan ordo matriks: "))

print("Masukkan elemen matriks baris per baris:")
A = []
for _ in range(n):
    row = [float(x) for x in input("Masukkan elemen baris (dipisahkan oleh spasi): ").split()]
    A.append(row)

b = [float(x) for x in input("Masukkan elemen vektor b dipisahkan oleh spasi: ").split()]

print("\nMatriks A:")
for row in A:
    print('[', ' '.join([str(e) for e in row]), ']')

print("\nVektor b:", b)

L = [[0 for row in range(n)] for col in range(n)]
U = [[0 for row in range(n)] for col in range(n)]

for p in range(n):
    for j in range(p, n):
        sum = 0
        for k in range(p):
            sum += L[p][k] * U[k][j]
        U[p][j] = A[p][j] - sum

    q = p
    for i in range(q, n):
        if i == q:
            L[i][q] = 1
        else:
            sum = 0
            for k in range(q):
                sum += L[i][k] * U[k][q]
            L[i][q] = (A[i][q] - sum) / U[q][q]

print("\nMatrix L :")
for row in L:
    print('[', ' '.join(['%.2f' % e for e in row]), ']')

print("\nMatrix U :")
for row in U:
    print('[', ' '.join(['%.2f' % e for e in row]), ']')

y = [0 for _ in range(n)]
for i in range(n):
    sum = 0
    for j in range(i):
        sum += L[i][j] * y[j]
    y[i] = (b[i] - sum) / L[i][i]

x = [0 for _ in range(n)]
for i in range(n-1, -1, -1):
    sum = 0
    for j in range(i+1, n):
        sum += U[i][j] * x[j]
    x[i] = (y[i] - sum) / U[i][i]

print("\nSolusi SPL:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.2f}")

def add_matrix(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            value = A[i][j] + B[i][j]
            row.append(value)
        result.append(row)
    return result


def multiply_matrix(A, B):
    rowA = len(A)
    colA = len(A[0])
    rowB = len(B)
    colB = len(B[0])

    if colA != rowB:
        print("Multiplication not possible ")
        return

    result = []
    for i in range(rowA):
        row = []
        for j in range(colB):
            sum = 0
            for k in range(colA):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)
    return result


def scalar_multip(matrix, scalar):
    result = []
    for i in matrix:
        new_row = []
        for x in i:
            value = scalar * x
            new_row.append(value)
        result.append(new_row)
    return result


A = [[1, 2], [3, 4]]
B = [[5, 6], [8, 9]]
scalar = 2

print("matrix A : ", A)
print("matrix B : ", B)
print("Addition : ", add_matrix(A, B))
print("Addition : ", add_matrix(A, B))
print("Multiplication : ", multiply_matrix(A, B))
print("scalar : ", scalar_multip(A, scalar))

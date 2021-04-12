import math
import numpy as np


def gauss(A, b, pivoteo=None):
    if A.shape[0] != A.shape[1]:
        print("Error, matriz no es cuadrada")
        return

    Ab = np.zeros((len(A), len(A) + 1))
    Ab[:, :-1] = A
    Ab[:, -1] = b

    n = Ab.shape[0]
    mark = list(range(n))

    procedimiento = []

    for row in range(n):
        err = None
        if pivoteo == "parcial":
            Ab, err = pivoteo_parcial(Ab, row)
        elif pivoteo == "total":
            Ab, mark, err = pivoteo_total(Ab, row, mark)
        if err:
            print(err)

        for col in range(row + 1, n):
            M = Ab[col, row] / Ab[row, row]
            for row_i in range(row, n + 1):
                Ab[col, row_i] -= M * Ab[row, row_i]

            procedimiento.append(Ab.copy())

    x = sustitucion_regresiva(Ab)
    x = [x[mark[i]] for i in range(n)]
    error = A.dot(x) - b
    return x, Ab, error, procedimiento


def sustitucion_regresiva(Ab):
    n = Ab.shape[0] - 1

    x = np.zeros(n + 1)
    x[n] = Ab[n, n + 1] / Ab[n, n]
    for i in range(n - 1, -1, -1):
        suma = sum(Ab[i, j] * x[j] for j in range(i + 1, n + 1))
        x[i] = (Ab[i, -1] - suma) / Ab[i, i]

    return x


def pivoteo_parcial(Ab, row):
    n = Ab.shape[0]

    mayor = abs(Ab[row, row])
    max_row = row
    for i in range(row + 1, n):
        if abs(Ab[i, row]) <= mayor:
            continue

        mayor = abs(Ab[i, row])
        max_row = i

    if mayor == 0:
        return Ab, "El sistema no tiene solución única"
    elif max_row != row:
        Ab[[row, max_row]] = Ab[[max_row, row]]

    return Ab, None


def pivoteo_total(Ab, row, mark):
    n = Ab.shape[0]

    mayor = 0
    max_row = row
    max_col = row
    for row_i in range(row, n):
        for col_i in range(row, n):
            if abs(Ab[row_i, col_i]) > mayor:
                mayor = abs(Ab[row_i, col_i])
                max_row = row_i
                max_col = col_i

    if mayor == 0:
        return Ab, mark, "El sistema no tiene solución única"
    if max_row != row:
        aux = Ab[row, :].copy()
        Ab[row, :] = Ab[max_row, :]
        Ab[max_row, :] = aux
    if max_col != row:
        aux = Ab[:, row].copy()
        Ab[:, row] = Ab[:, max_col]
        Ab[:, max_col] = aux
        aux2 = mark[row]
        mark[row] = mark[max_col]
        mark[max_col] = aux2

    return Ab, mark, None


# A = np.array([[1, 2, 3], [4, 5, 6], [7, 87, 9]])
# b = np.array([3, 4, 5])
# A = np.array([[-7, 2, -3, 4], [5, -1, 14, -1], [1, 9, -7, 5], [-12, 13, -8, -4]])
# b = np.array([-12, 13, 31, -32])
A = np.array([[1, 2.3, 3.1], [25, 30, 15], [100, 200, 300]])
b = np.array([13, 25, 28])
x, Ab, error, procedimiento = gauss(A, b)
# print(x, error)
# print(np.linalg.norm(error))

x, Ab, error, procedimiento = gauss(A, b, pivoteo="parcial")
# print(x, error)
print(np.linalg.norm(error))

# np.invert(Ab)

print(x)
x, Ab, error, procedimiento = gauss(A, b, pivoteo="total")
# # print(x, error)
print(np.linalg.norm(error))


# Ab = np.zeros((len(A), len(A) + 1))
# Ab[:, :-1] = A
# Ab[:, -1] = b

# pivoteo_parcial(Ab, 0)
# pivoteo_parcial(Ab, 1)
# pivoteo_parcial(Ab, 2)
# pivoteo_parcial(Ab, 3)

# print(Ab)

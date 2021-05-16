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

            procedimiento.append(Ab.copy().tolist())

    x = sustitucion_regresiva(Ab)
    x = [x[mark[i]] for i in range(n)]

    error = A.dot(x) - b
    return x, Ab.tolist(), error.tolist(), procedimiento


def LU(A, b, pivoteo=None):
    n = A.shape[0]
    P = np.eye(n)
    L = np.eye(n)

    for k in range(n - 1):

        if pivoteo == "parcial":
            A, P = pivoteoLU(A, P, k)

        for i in range(k + 1, n):
            M = A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] -= M * A[k, j]

            A[i, k] = M

    U = np.triu(A)
    L = L + np.tril(A, -1)
    B = P.dot(b)

    LB = np.zeros((len(L), len(L) + 1))
    LB[:, :-1] = L
    LB[:, -1] = b

    z = sustpro(LB)

    Uz = np.zeros((len(U), len(U) + 1))
    Uz[:, :-1] = U
    Uz[:, -1] = z

    x = sustreg(Uz)

    return x, L, U


def LUdirecto(A, met):
    n = A.shape[0]
    U = np.eye(n)
    L = np.eye(n)

    for k in range(n):
        sum1 = sum(L[k, p] * U[p, k] for p in range(k))
        if met == 0:
            U[k, k] = (A[k, k] - sum1) / L[k, k]
        elif met == 1:
            L[k, k] = (A[k, k] - sum1) / U[k, k]
        else:
            U[k, k] = np.sqrt(A[k, k] - sum1)
            L[k, k] = U[k, k]

        for i in range(k, n):
            sum2 = sum(L[i, p] * U[p, k] for p in range(k))
            L[i, k] = (A[i, k] - sum2) / U[k, k]

        for j in range(k, n):
            sum3 = sum(L[k, p] * U[p, j] for p in range(k))
            U[k, j] = (A[k, j] - sum3) / L[k, k]

    return L, U


def pivoteoLU(A, P, row):
    n = A.shape[0]

    mayor = abs(A[row, row])
    maxrow = row
    for i in range(row + 1, n):
        if abs(A[i, row]) > mayor:
            mayor = abs(A[i, row])
            maxrow = i

    if mayor == 0:
        return A, P, "El sistema no tiene solución única"

    if maxrow != row:  # Intercambio de filas
        aux = A[row, :]
        auxP = P[row, :]
        A[row, :] = A[maxrow, :]
        P[row, :] = P[maxrow, :]
        A[maxrow, :] = aux
        P[maxrow, :] = auxP

    return A, P, None


def mathJacobiSeidel(x0, A, b, tol, n_iter_max, method):

    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, +1)

    message = ""
    errores = [tol + 1]
    itera = [x0]

    for _ in range(n_iter_max):
        if errores[-1] <= tol:
            message = f"{x0} es una aproximación de la solución del sistema con una tolerancia= {tol}"
            break

        if method == "jacobi":
            T = np.linalg.inv(D).dot(L + U)
            C = np.linalg.inv(D).dot(b)
            x1 = T.dot(x0) + C
        elif method == "seidel":
            T = np.linalg.inv(D - L).dot(U)
            C = np.linalg.inv(D - L).dot(b)
            x1 = T.dot(x0) + C

        # errores.append(np.linalg.norm(x1 - x0))
        itera.append(x0)
        x0 = x1
    else:
        message = f"Fracasó en {n_iter_max} iteraciones"

    return errores, x0, message, itera


def iterativos(x0, A, b, tol, n_iter_max, method):

    message = ""
    errores = [tol + 1]

    for _ in range(n_iter_max):
        if errores[-1] <= tol:
            message = f"{x0} es una aproximación de la solución del sistema con una tolerancia= {tol}"
            break

        x1 = new_jacobi(x0, A, b) if method == "jacobi" else new_seidel(x0, A, b)
        errores.append(np.linalg.norm(x1 - x0))
        x0 = x1.copy()
    else:
        message = f"Fracasó en {n_iter_max} iteraciones"

    return x0.tolist(), message, errores


def new_jacobi(x0, A, b):
    n = A.shape[0]
    x1 = x0.copy()
    for i in range(n):
        suma = sum(A[i, j] * x0[j] for j in range(n) if j != i)
        x1[i] = (b[i] - suma) / A[i, i]

    return x1


def new_seidel(x0, A, b):

    n = A.shape[0]
    x1 = x0.copy()
    for i in range(n):
        suma = sum(A[i, j] * x1[j] for j in range(n) if j != i)
        x1[i] = (b[i] - suma) / A[i, i]

    return x1


def sustitucion_regresiva(Ab):
    n = Ab.shape[0] - 1

    x = np.zeros(n + 1)
    x[n] = Ab[n, n + 1] / Ab[n, n]
    for i in range(n - 1, -1, -1):
        suma = sum(Ab[i, j] * x[j] for j in range(i + 1, n + 1))
        x[i] = (Ab[i, -1] - suma) / Ab[i, i]

    return x


def sustitucion_progresiva(Ab):
    n = Ab.shape[0] - 1
    x = np.zeros(n + 1)
    x[0] = Ab[0, n + 1] / Ab[1, 1]

    for i in range(1, n):
        suma = sum(Ab[i, j] * x[j] for j in range(i - 1))
        x[i] = (Ab[i, n + 1] - suma) / Ab[i, i]

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
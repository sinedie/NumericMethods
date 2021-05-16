import sympy
import numpy as np
from .utils import parse_pol


def lagrange(x, y):
    n = len(x)
    tabla = np.zeros((n, n))
    for i in range(n):
        Li = 1
        den = 1
        for j in range(n):
            if j != i:
                paux = [1, -x[j]]
                Li = np.convolve(Li, paux)
                den *= x[i] - x[j]

        tabla[i, :] = y[i] * Li / den

    pols = [sum(tabla).tolist()]
    polinomio = parse_pol(pols)
    return polinomio, pols


def diferencias_newton(x, y):
    n = len(x)
    tabla = np.zeros((n, n + 1))
    tabla[:, 0] = x
    tabla[:, 1] = y
    for j in range(2, n + 1):
        for i in range(j - 1, n):
            denominador = tabla[i, 0] - tabla[i - j + 1, 0]
            tabla[i, j] = (tabla[i, j - 1] - tabla[i - 1, j - 1]) / denominador

    pol = 0
    coef = np.diag(tabla[:, 1:])
    x_symbol = sympy.Symbol("x")
    for i in range(len(coef)):
        const = coef[i]
        for j in range(i):
            const *= x_symbol - x[j]
        pol += const

    return [str(sympy.simplify(pol))], tabla.tolist()


def spline_lineal(x, y):
    d = 1
    n = len(x)
    A = np.zeros(((d + 1) * (n - 1), (d + 1) * (n - 1)))
    b = np.zeros(((d + 1) * (n - 1), 1))

    c = 0
    h = 0
    for i in range(n - 1):
        A[i, c] = x[i]
        A[i, c + 1] = 1
        b[i] = y[i]
        c += 2
        h += 1

    c = 0
    for i in range(1, n):
        A[h, c] = x[i]
        A[h, c + 1] = 1
        b[h] = y[i]
        c += 2
        h += 1

    val = np.dot(np.linalg.inv(A), b)
    pols = np.reshape(val, (n - 1, d + 1))
    polinomios = parse_pol(pols)
    return polinomios, pols.tolist()


def spline_cuadratico(x, y):
    d = 2
    n = len(x)
    A = np.zeros(((d + 1) * (n - 1), (d + 1) * (n - 1)))
    b = np.zeros(((d + 1) * (n - 1), 1))
    cua = x ** 2

    c = 0
    h = 0
    for i in range(n - 1):
        A[i, c] = cua[i]
        A[i, c + 1] = x[i]
        A[i, c + 2] = 1
        b[i] = y[i]
        c += 3
        h += 1

    c = 0
    for i in range(1, n):
        A[h, c] = cua[i]
        A[h, c + 1] = x[i]
        A[h, c + 2] = 1
        b[h] = y[i]
        c += 3
        h += 1

    c = 0
    for i in range(1, n - 1):
        A[h, c] = 2 * x[i]
        A[h, c + 1] = 1
        A[h, c + 3] = -2 * x[i]
        A[h, c + 4] = -1
        b[h] = 0
        c += 4
        h += 1

    A[h, 0] = 2
    b[h] = 0

    val = np.dot(np.linalg.inv(A), b)
    pols = np.reshape(val, (n - 1, d + 1))
    polinomios = parse_pol(pols)
    return polinomios, pols.tolist()


def spline_cubico(x, y):
    d = 3
    n = len(x)
    A = np.zeros(((d + 1) * (n - 1), (d + 1) * (n - 1)))
    b = np.zeros(((d + 1) * (n - 1), 1))
    cua = x ** 2
    cub = x ** 3

    c = 0
    h = 0
    for i in range(n - 1):
        A[i, c : c + 4] = [cub[i], cua[i], x[i], 1]
        b[i] = y[i]
        c += 4
        h += 1

    c = 0
    for i in range(1, n):
        A[h, c : c + 4] = [cub[i], cua[i], x[i], 1]
        b[h] = y[i]
        c += 4
        h += 1

    c = 0
    for i in range(1, n - 1):
        A[h, c] = 3 * cua[i]
        A[h, c + 1] = 2 * x[i]
        A[h, c + 2] = 1

        A[h, c + 4] = -3 * cua[i]
        A[h, c + 5] = -2 * x[i]
        A[h, c + 6] = -1
        b[h] = 0
        c += 4
        h += 1

    c = 0
    for i in range(1, n - 1):
        A[h, c] = 6 * x[i]
        A[h, c + 1] = 2
        A[h, c + 4] = -6 * x[i]
        A[h, c + 5] = -2
        b[h] = 0
        c += 4
        h += 1

    A[h, 0] = 6 * x[0]
    A[h, 1] = 2
    b[h] = 0
    h += 1
    A[h, c] = 6 * x[-1]
    A[h, c + 1] = 2
    b[h] = 0

    val = np.dot(np.linalg.inv(A), b)
    pols = np.reshape(val, (n - 1, d + 1))
    polinomios = parse_pol(pols)
    return polinomios, pols.tolist()

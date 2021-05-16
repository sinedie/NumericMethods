import math
import base64
import sympy
import numpy as np
from matplotlib.figure import Figure
from io import BytesIO


def graphic_method(f, f_str, fp, fp_str, x_a, x_b, step=100):

    x = [x for x in np.linspace(x_a, x_b, step)]
    y = [f(x) for x in np.linspace(x_a, x_b, step)]
    yp = [fp(x) for x in np.linspace(x_a, x_b, step)]

    fig = Figure()
    ax = fig.subplots()

    # ax.title = "Metodo grafico"
    ax.xlabel = "x"
    ax.ylabel = "y"
    ax.plot(x, y, label=f"f(x)={f_str}")
    ax.plot(x, yp, "--", label=f"f'(x)={fp_str}")
    ax.legend()
    ax.grid()

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")

    return base64.b64encode(buf.getbuffer()).decode("ascii")


def bi(x_inicial, f, delta=0.001, n_iter_max=1000):

    x_a = x_inicial
    f_a = f(x_a)

    raiz = None
    message = None
    results = [[x_a, f_a]]

    if f_a == 0:
        message = f"{x_a} es raiz de f(x)"
        raiz = x_a

    x_b = x_inicial + delta
    f_b = f(x_b)

    for _ in range(n_iter_max):
        if f_a * f_b < 0:
            message = f"Existe una raiz de f(x) entre {x_a} y {x_b}"
            raiz = [x_a, x_b]

        x_a = x_b
        f_a = f_b

        results.append([x_a, f_a])

        x_b += delta
        f_b = f(x_b)

        if f_b == 0:
            message = f"{x_b} es raiz de f(x)"
            raiz = x_b

    else:
        print(f"Fracaso en {n_iter_max} iteraciones ")

    return raiz, message, results


def biseccion(x_a, x_b, f, tol=1e-6, err="abs", regla_falsa=False, n_iter_max=1000):

    f_a = f(x_a)
    f_b = f(x_b)

    raiz = None
    message = None
    results = []

    if f_a == 0:
        message = f"{x_a} es raiz de f(x)"
        raiz = x_a

    elif f_b == 0:
        message = f"{x_b} es raiz de f(x)"
        raiz = x_b

    elif f_a * f_b > 0:
        message = f"No existe raiz en el intervalo [{x_a}, {x_b}]"

    if message is not None:
        return raiz, message, results

    x_m = (f_b * x_a - f_a * x_b) / (f_b - f_a) if regla_falsa else (x_a + x_b) / 2
    f_m = f(x_m)
    results = [[x_m, f_m, 100]]

    for _ in range(n_iter_max):
        if f_a * f_m < 0:
            x_b = x_m
            f_b = f(x_b)
        else:
            x_a = x_m
            f_a = f(x_a)

        x_c = (f_b * x_a - f_a * x_b) / (f_b - f_a) if regla_falsa else (x_a + x_b) / 2
        error = abs((x_c - x_m) / (x_m if err == "rel" else 1))
        x_m = x_c
        f_m = f(x_m)

        results.append([x_m, f_m, error])

        if f_m == 0:
            message = f"{x_m} es raiz de f(x)"
            raiz = x_m
            break

        if error < tol:
            message = f"{x_m} es una aproximacion de una raiz de f(x) con una tolerancia {tol}"
            raiz = x_m
            break
    else:
        message = f"Fracaso en {n_iter_max} iteraciones "

    return raiz, message, results


def n_iter_biseccion(x_a, x_b, x_raiz, x_mf):

    return math.floor(math.log(abs((x_b - x_a) / (x_mf - x_raiz)), 2))


def punto_fijo(x_a, f, g, tol=1e-6, err="abs", n_iter_max=1000):

    f_a = f(x_a)

    # x_a, f_a, err_a
    results = [[x_a, f_a, 100]]

    for _ in range(n_iter_max):
        x_b = g(x_a)
        error = abs((x_b - x_a) / (x_a if err == "rel" else 1))

        x_a = x_b
        f_a = f(x_a)

        results.append([x_a, f_a, error])

        if f_a == 0:
            message = f"{x_a} es raiz de f(x)"
            break
        elif error < tol:
            message = f"{x_a} es una aproximacion de una raiz de f(x) con una tolerancia {tol}"
            break

    else:
        message = f"Fracaso en {n_iter_max} iteraciones"

    return x_a, message, results


def n_iter_punto_fijo(x_a, x_b, k, x_0, error):

    return math.floor(np.log(error / max(x_0 - x_a, x_b - x_0)) / np.log(k))


def newton_raphson(x_a, f, fp, m=1, tol=1e-6, err="abs", n_iter_max=1000):

    f_a = f(x_a)
    fp_a = fp(x_a)
    results = [[x_a, f_a, fp_a, 100]]
    message = None

    for _ in range(n_iter_max):
        if fp_a == 0:
            message = f"La derivada de la f(x) en {x_a} es cero"
            break

        x_b = x_a - m * f_a / fp_a

        error = abs((x_b - x_a) / (x_a if err == "rel" else 1))

        x_a = x_b
        f_a = f(x_a)
        fp_a = fp(x_a)

        results.append([x_a, f_a, fp_a, error])

        if f_a == 0:
            message = f"{x_a} es raiz de f(x)"
            break

        elif error < tol:
            message = f"{x_a} es una aproximacion de una raiz de f(x) con una tolerancia {tol}"
            break
    else:
        message = f"Fracaso en {n_iter_max} iteraciones"

    return x_a, message, results


def newton_raphson_multiples_raices(
    x_a, f, fp, fpp, tol=1e-6, err="abs", n_iter_max=1000
):

    f_a = f(x_a)
    fp_a = fp(x_a)
    fpp_a = fpp(x_a)
    results = [[x_a, f_a, fp_a, fpp_a, 100]]
    message = None

    for _ in range(n_iter_max):
        if fp_a == 0:
            message = f"La derivada de la f(x) en {x_a} es cero"
            break

        x_b = x_a - f_a * fp_a / (fp_a ** 2 - f_a * fpp_a)

        error = abs((x_b - x_a) / (x_a if err == "rel" else 1))

        x_a = x_b
        f_a = f(x_a)
        fp_a = fp(x_a)

        results.append([x_a, f_a, fp_a, fpp_a, error])

        if f_a == 0:
            message = f"{x_a} es raiz de f(x)"
            break

        elif error < tol:
            message = f"{x_a} es una aproximacion de una raiz de f(x) con una tolerancia {tol}"
            break
    else:
        message = f"Fracaso en {n_iter_max} iteraciones"

    return x_a, message, results


def secante(x_a, x_b, f, tol=1e-6, err="abs", n_iter_max=1000):
    # x_a debe ser menor que x_b

    f_a = f(x_a)
    f_b = f(x_b)
    results = [[x_a, f_a, 100], [x_b, f_b, 100]]
    message = None

    for _ in range(n_iter_max):
        x_c = x_b - f_b * (x_b - x_a) / (f_b - f_a)

        error = abs((x_c - x_b) / (x_b if err == "rel" else 1))

        x_a = x_b
        x_b = x_c
        f_a = f_b
        f_b = f(x_c)

        results.append([x_b, f_b, error])

        if f_a == 0:
            message = f"{x_a} es raiz de f(x)"
            break

        elif error < tol:
            message = f"{x_a} es una aproximacion de una raiz de f(x) con una tolerancia {tol}"
            break
    else:
        message = f"Fracaso en {n_iter_max} iteraciones"

    return x_a, message, results


def check_n_raices(f, x):
    fp = sympy.diff(get_expr(f))

    n_raices = 1
    while parse_function(fp)(x) == 0:
        n_raices += 1
        fp = sympy.diff(fp)

    return n_raices

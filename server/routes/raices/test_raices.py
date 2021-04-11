from expr_parser import parse_function, parse_expr
from raices import (
    graphic_method,
    bi,
    biseccion,
    n_iter_biseccion,
    punto_fijo,
    n_iter_punto_fijo,
    newton_raphson,
)

function = "exp(x)/x+3"
function_g = "-exp(x)/3"
result = -22
x_a = -1
x_b = 0


def test_parser():
    f = parse_function(function)
    assert callable(f)


def test_graphic_method():
    graphic_method(function, x_a, x_b)


def test_bi():
    raiz, message, results = bi(x_a, function, 0.01)
    print(message)
    if type(raiz) is list:
        assert raiz[0] < result and raiz[1] > result
    else:
        assert abs(raiz - result) < 1e-3


def test_biseccion():
    raiz, message, results = biseccion(x_a, x_b, function)
    print(message)
    assert raiz == result


def test_punto_fijo():
    raiz, message, results = punto_fijo(x_a, function, function_g)
    print(results)
    print(message)
    assert raiz == result


def test_n_iter_punto_fijo():
    # n_iter = n_iter_punto_fijo(x_a, x_b, k, x_0, error)
    n_iter = n_iter_punto_fijo(-3, -1, 0.7, -0.5, 0.5 * 1e-3)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", n_iter)


def test_newton_raphson():
    raiz, message, results = newton_raphson(x_a, function, tol=1e-10)
    print(results)
    print(message)
    assert abs(raiz - result) < 1e-6

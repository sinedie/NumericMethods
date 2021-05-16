def trapecio(f, a, b, n):
    h = abs(b - a) / n
    suma = sum(2 * f(a + i * h) for i in range(1, n))
    suma += f(a) + f(b)
    return suma * h / 2


def simpson(f, a, b, n):
    h = abs(b - a) / n
    suma = sum((2 if i % 2 == 0 else 4) * f(a + i * h) for i in range(1, n))
    suma += f(a) + f(b)
    return suma * h / 3

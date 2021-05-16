import sympy


def beta_fc(fc):

    if fc <= 280:
        return 0.85
    if fc >= 560:
        return 0.65

    return (280 - fc) / 1400 + 0.85


def revisar_seccion(base, altura, dp, As, Asp, fc, fy=4200, E=2000000, ec_max=0.003):
    d = altura - dp
    beta = beta_fc(fc)
    x = sympy.Symbol("x")
    c = ec_max * d / x + ec_max
    fs = E * (x + ec_max) * (c - dp) / d

    f = 0.85 * fc * beta * c * base - 0.85 * fc * Asp + Asp * fs - As * fy
    f = sympy.simplify(f)
    print(f)


revisar_seccion(40, 40, 5, 10, 20, 210)
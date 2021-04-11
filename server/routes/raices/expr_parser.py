import sympy
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    function_exponentiation,
    implicit_multiplication_application,
)


def get_expr(function):

    return parse_expr(
        function,
        transformations=(
            standard_transformations
            + (
                function_exponentiation,
                implicit_multiplication_application,
            )
        ),
    )


def parse_function(f):
    if isinstance(f, str):
        f = get_expr(f)

    def f_func(x):
        result = f.subs({"x": x})
        return float(result)

    return f_func

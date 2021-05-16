import sympy
from flask import Blueprint, request, jsonify

from server.metodos import (
    graphic_method,
    bi,
    biseccion,
    n_iter_biseccion,
    n_iter_punto_fijo,
    punto_fijo,
    newton_raphson,
    newton_raphson_multiples_raices,
    secante,
    check_n_raices,
    parse_function,
    get_expr,
)

raices = Blueprint("raices", __name__, url_prefix="/api/raices")


@raices.route("/grafico", methods=["POST"])
def _grafico():
    fp_str = sympy.diff(get_expr(request.json["func"]))

    return jsonify(
        image=graphic_method(
            f=parse_function(request.json["func"]),
            f_str=request.json["func"],
            fp=parse_function(fp_str),
            fp_str=fp_str,
            x_a=float(request.json["xi"]),
            x_b=float(request.json["xf"]),
            step=100,
        )
    )


@raices.route("/biseccion", methods=["POST"])
def _biseccion():
    return jsonify(
        raiz=biseccion(
            x_a=float(request.json["xi"]),
            x_b=float(request.json["xf"]),
            f=parse_function(request.json["func"]),
            tol=float(request.json["tol"]),
            err=request.json["err"],
            regla_falsa=request.json["regla_falsa"],
            n_iter_max=int(request.json["n_max_iter"]),
        )
    )


@raices.route("/punto_fijo", methods=["POST"])
def _punto_fijo():
    return jsonify(
        raiz=punto_fijo(
            x_a=float(request.json["xi"]),
            f=parse_function(request.json["func"]),
            g=parse_function(request.json["func_g"]),
            tol=float(request.json["tol"]),
            err=request.json["err"],
            n_iter_max=int(request.json["n_max_iter"]),
        )
    )


@raices.route("/newton", methods=["POST"])
def _newton():
    return jsonify(
        raiz=newton_raphson(
            x_a=float(request.json["xi"]),
            f=parse_function(request.json["func"]),
            fp=parse_function(sympy.diff(get_expr(request.json["func"]))),
            m=int(request.json["multiplicidad_raiz"]),
            tol=float(request.json["tol"]),
            err=request.json["err"],
            n_iter_max=int(request.json["n_max_iter"]),
        )
    )


@raices.route("/newton_multiple", methods=["POST"])
def _newton_mul():
    fp = sympy.diff(get_expr(request.json["func"]))

    return jsonify(
        raiz=newton_raphson_multiples_raices(
            x_a=float(request.json["xi"]),
            f=parse_function(request.json["func"]),
            fp=parse_function(fp),
            fpp=parse_function(sympy.diff(fp)),
            tol=float(request.json["tol"]),
            err=request.json["err"],
            n_iter_max=int(request.json["n_max_iter"]),
        )
    )


@raices.route("/secante", methods=["POST"])
def _secante():
    return jsonify(
        raiz=secante(
            x_a=float(request.json["xi"]),
            x_b=float(request.json["xf"]),
            f=parse_function(request.json["func"]),
            tol=float(request.json["tol"]),
            err=request.json["err"],
            n_iter_max=int(request.json["n_max_iter"]),
        )
    )

from flask import Blueprint, request, jsonify

from .routines import graphic_method, biseccion, punto_fijo, newton_raphson, secante

raices = Blueprint("raices", __name__, url_prefix="/api/raices")


@raices.route("/grafico", methods=["POST"])
def get_from_grafico():
    image = graphic_method(
        request.json["func"],
        float(request.json["xi"]),
        float(request.json["xf"]),
        step=100,
    )
    return jsonify(image=image)


@raices.route("/biseccion", methods=["POST"])
def get_from_biseccion():
    print(request.json)
    raiz, message, results = biseccion(
        float(request.json["xi"]),
        float(request.json["xf"]),
        request.json["func"],
        tol=float(request.json["tol"]),
        err=request.json["err"],
        regla_falsa=request.json["regla_falsa"],
        n_iter_max=int(request.json["n_max_iter"]),
    )

    return jsonify(raiz=raiz, message=message, results=results)


@raices.route("/punto-fijo", methods=["POST"])
def get_from_punto_fijo():
    raiz, message, results = punto_fijo(
        float(request.json["xi"]),
        request.json["func"],
        request.json["func_g"],
        tol=float(request.json["tol"]),
        err=request.json["err"],
        n_iter_max=int(request.json["n_max_iter"]),
    )

    return jsonify(raiz=raiz, message=message, results=results)


@raices.route("/newton", methods=["POST"])
def get_from_newton():
    raiz, message, results = newton_raphson(
        float(request.json["xi"]),
        request.json["func"],
        int(request.json["multiplicidad_raiz"]),
        tol=float(request.json["tol"]),
        err=request.json["err"],
        n_iter_max=int(request.json["n_max_iter"]),
    )

    return jsonify(raiz=raiz, message=message, results=results)


@raices.route("/secante", methods=["POST"])
def get_from_secante():
    raiz, message, results = secante(
        float(request.json["xi"]),
        float(request.json["xf"]),
        request.json["func"],
        tol=float(request.json["tol"]),
        err=request.json["err"],
        n_iter_max=int(request.json["n_max_iter"]),
    )

    return jsonify(raiz=raiz, message=message, results=results)

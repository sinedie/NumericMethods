from flask import Blueprint, request, jsonify

from server.metodos import simpson, trapecio, parse_function

integracion = Blueprint("integracion", __name__, url_prefix="/api/integracion")


@integracion.route("/simpson", methods=["POST"])
def _simpson():
    return jsonify(
        integral=simpson(
            f=parse_function(request.json["func"]),
            a=float(request.json["xi"]),
            b=float(request.json["xf"]),
            n=int(request.json["n"]),
        )
    )


@integracion.route("/trapecio", methods=["POST"])
def _trapecio():
    return jsonify(
        integral=trapecio(
            f=parse_function(request.json["func"]),
            a=float(request.json["xi"]),
            b=float(request.json["xf"]),
            n=int(request.json["n"]),
        )
    )

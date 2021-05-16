import sympy
import numpy as np
from flask import Blueprint, request, jsonify

from server.metodos import (
    lagrange,
    diferencias_newton,
    spline_lineal,
    spline_cuadratico,
    spline_cubico,
)

interpolacion = Blueprint("interpolacion", __name__, url_prefix="/api/interpolacion")


def getPoints(x, y):
    return [np.array([float(v) for v in x]), np.array([float(v) for v in y])]


@interpolacion.route("/lagrange", methods=["POST"])
def _lagrange():
    return jsonify(
        interpolacion=lagrange(*getPoints(request.json["x"], request.json["y"]))
    )


@interpolacion.route("/spline_lineal", methods=["POST"])
def _spline_lineal():
    return jsonify(
        interpolacion=spline_lineal(*getPoints(request.json["x"], request.json["y"]))
    )


@interpolacion.route("/spline_cuadratico", methods=["POST"])
def _spline_cuadratico():
    return jsonify(
        interpolacion=spline_cuadratico(
            *getPoints(request.json["x"], request.json["y"])
        )
    )


@interpolacion.route("/spline_cubico", methods=["POST"])
def _spline_cubico():
    return jsonify(
        interpolacion=spline_cubico(*getPoints(request.json["x"], request.json["y"]))
    )


@interpolacion.route("/newton", methods=["POST"])
def _newton():
    return jsonify(
        interpolacion=diferencias_newton(
            *getPoints(request.json["x"], request.json["y"])
        )
    )

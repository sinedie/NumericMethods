import numpy as np
from flask import Blueprint, request, jsonify
from server.metodos import gauss, iterativos

ecuaciones = Blueprint("ecuaciones", __name__, url_prefix="/api/ecuaciones")


@ecuaciones.route("/gauss", methods=["POST"])
def _gauss():
    return jsonify(
        results=gauss(
            np.array([[float(v) for v in row] for row in request.json["A"]]),
            np.array([float(v) for v in request.json["b"]]),
            request.json["pivoteo"],
        )
    )


@ecuaciones.route("/seidel", methods=["POST"])
def _seidel():
    return jsonify(
        results=iterativos(
            np.array([float(v) for v in request.json["x0"]]),
            np.array([[float(v) for v in row] for row in request.json["A"]]),
            np.array([float(v) for v in request.json["b"]]),
            float(request.json["tol"]),
            int(request.json["n_iter_max"]),
            "seidel",
        )
    )


@ecuaciones.route("/jacobi", methods=["POST"])
def _jacobi():
    return jsonify(
        results=iterativos(
            np.array([float(v) for v in request.json["x0"]]),
            np.array([[float(v) for v in row] for row in request.json["A"]]),
            np.array([float(v) for v in request.json["b"]]),
            float(request.json["tol"]),
            int(request.json["n_iter_max"]),
            "jacobi",
        )
    )

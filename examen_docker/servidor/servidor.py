from flask import Flask, request, jsonify
import requests
from xmlrpc.server import SimpleXMLRPCServer

app = Flask(__name__)

SERVICIOS = {
    "suma": "http://listar:5001/listar",
    "resta": "http://crear:5002/crear",
    "multiplicacion": "http://actualizar:5003/actualizar",
    "division": "http://eliminar:5004/eliminar"
}

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json
    operacion = data.get("operacion")
    a = data.get("a")
    b = data.get("b")

    if operacion not in SERVICIOS:
        return jsonify({
            "error": "Operación no válida"
        }), 400

    respuesta = requests.post(
        SERVICIOS[operacion],
        json={"a": a, "b": b}
    )

    return jsonify(respuesta.json()), respuesta.status_code

if __name__ == "__main__":
    server = SimpleXMLRPCServer(("0.0.0.0", 8000))
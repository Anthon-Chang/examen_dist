from flask import Flask, request, jsonify
import requests
import xmlrpc.client

app = Flask(__name__)


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


def menu():
    while opciones != 5:
        print("---menu---")
        print("1. listar pelicula")
        print("2. crear pelicula")
        print("3. actualizar pelicula")
        print("4. eliminar pelicula")
        print("5. salir")

        opciones = input("Eligue una opcion")

        if opciones == "1":
            listar()
        elif opciones == "2":
            crear()
        elif opciones == "3":
            actualizar()
        elif opciones == "4":
            eliminar()
        elif opciones == "5":
            print("salir...")
        else:
            print("numero invalido")

def listar():
    for x in peliculas:
        print(x)

def crear():






if __name__ == "__main__":
    cliente = xmlrpc.client.ServerProxy("http://servidor:8000/")
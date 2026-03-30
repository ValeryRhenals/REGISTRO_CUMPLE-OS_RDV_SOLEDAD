import json

def cargar_clientes():
    try:
        with open("clientes.json", "r") as archivo:
            return json.load(archivo)
    except:
        return {}

def guardar_clientes(clientes):
    with open("clientes.json", "w") as archivo:
        json.dump(clientes, archivo, indent=4)
from database import guardar_clientes

def crear_cliente(clientes):
    print("Ingrese la informacion del cliente")
    id = input("Id: ")

    if id in clientes:
        print("Error: el cliente ya existe.")
        return

    nombre = input("Nombre: ")
    edad = input("Edad: ")
    plan = input("Plan: ")
    estado = input("Estado: ")

    clientes[id] = {
        "id": id,
        "nombre": nombre,
        "edad": edad,
        "plan": plan,
        "estado": estado
    }

    guardar_clientes(clientes)
    print("Cliente guardado correctamente")


def listar_clientes(clientes):
    if not clientes:
        print("_NO HAY CLIENTES GUARDADOS")
        return

    for id, datos in clientes.items():
        print(f"\nID: {id}")
        print(f"Nombre: {datos['nombre']}")


def buscar_cliente(clientes):
    id_buscar = input("ID: ")

    if id_buscar in clientes:
        print(clientes[id_buscar])
    else:
        print("No encontrado")


def actualizar_cliente(clientes):
    id_buscar = input("ID: ")

    if id_buscar in clientes:
        nombre = input("Nuevo nombre: ")
        clientes[id_buscar]["nombre"] = nombre

        guardar_clientes(clientes)
        print("Actualizado")
    else:
        print("No encontrado")


def eliminar_cliente(clientes):
    id_buscar = input("ID: ")

    if id_buscar in clientes:
        del clientes[id_buscar]
        guardar_clientes(clientes)
        print("Eliminado")
    else:
        print("No encontrado")
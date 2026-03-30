import os
from database import cargar_clientes
from clientes import *

def limpiar():
    os.system("cls")

clientes = cargar_clientes()

while True:
    print("MENU")
    print("1. Guardar cliente.")
    print("2. Lista de clientes.")
    print("3. Buscar cliente en especifico.")
    print("4. Actualizar cliente en especifico.")
    print("5. Eliminar un cliente.")
    print("6. Salir del sistema")

    opcion = input("Elige una opion de (1/6): ")

    if opcion == "1":
        crear_cliente(clientes)
        
    elif opcion == "2":
        listar_clientes(clientes)
        
    elif opcion == "3":
        buscar_cliente(clientes)
        
    elif opcion == "4":
        actualizar_cliente(clientes)
        
    elif opcion == "5":
        eliminar_cliente(clientes)
        
    elif opcion == "6":
        break
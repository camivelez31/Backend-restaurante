import requests

BASE_URL = "http://127.0.0.1:8000/clientes/"


def listar_clientes():
   
    respuesta = requests.get(BASE_URL)

    if respuesta.status_code == 200:
        clientes = respuesta.json()

        if not clientes:
            print("\nNo hay clientes registrados.\n")
            return

        print("\n--- LISTA DE CLIENTES ---")
        for cliente in clientes:
            print(
                f"ID: {cliente['id']} | "
                f"Nombre: {cliente['nombre']} | "
                f"Telefono: {cliente['telefono']} | "
                f"Correo: {cliente['correo']}"
            )
        print()
    else:
        print("\nError al listar clientes.\n")


def obtener_cliente():
    
    cliente_id = input("Ingrese el ID del cliente: ")

    respuesta = requests.get(f"{BASE_URL}{cliente_id}")

    if respuesta.status_code == 200:
        cliente = respuesta.json()
        print("\n--- CLIENTE ENCONTRADO ---")
        print(f"ID: {cliente['id']}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Telefono: {cliente['telefono']}")
        print(f"Correo: {cliente['correo']}\n")
    else:
        print("\nCliente no encontrado.\n")


def crear_cliente():
    
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el telefono: ")
    correo = input("Ingrese el correo: ")

    datos = {
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo
    }

    respuesta = requests.post(BASE_URL, json=datos)

    if respuesta.status_code == 201:
        cliente = respuesta.json()
        print("\nCliente creado correctamente.")
        print(f"ID asignado: {cliente['id']}\n")
    else:
        print("\nError al crear cliente.")
        print(respuesta.text)
        print()


def actualizar_cliente():
   
    cliente_id = input("Ingrese el ID del cliente a actualizar: ")
    nombre = input("Nuevo nombre (deje vacío si no desea cambiarlo): ")
    telefono = input("Nuevo telefono (deje vacío si no desea cambiarlo): ")
    correo = input("Nuevo correo (deje vacío si no desea cambiarlo): ")

    datos = {}

    if nombre:
        datos["nombre"] = nombre
    if telefono:
        datos["telefono"] = telefono
    if correo:
        datos["correo"] = correo

    respuesta = requests.put(f"{BASE_URL}{cliente_id}", json=datos)

    if respuesta.status_code == 200:
        print("\nCliente actualizado correctamente.\n")
    else:
        print("\nError al actualizar cliente.\n")


def eliminar_cliente():
   
    cliente_id = input("Ingrese el ID del cliente a eliminar: ")

    respuesta = requests.delete(f"{BASE_URL}{cliente_id}")

    if respuesta.status_code == 200:
        print("\nCliente eliminado correctamente.\n")
    else:
        print("\nError al eliminar cliente.\n")
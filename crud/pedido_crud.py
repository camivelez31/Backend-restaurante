import requests

BASE_URL = "http://127.0.0.1:8000/pedidos/"


def listar_pedidos():
  
    respuesta = requests.get(BASE_URL)

    if respuesta.status_code == 200:
        pedidos = respuesta.json()

        if not pedidos:
            print("\nNo hay pedidos registrados.\n")
            return

        print("\n--- LISTA DE PEDIDOS ---")
        for pedido in pedidos:
            print(
                f"ID: {pedido['id']} | "
                f"Estado: {pedido['estado']} | "
                f"Fecha: {pedido['fecha']} | "
                f"Cliente ID: {pedido['cliente_id']} | "
                f"Empleado ID: {pedido['empleado_id']} | "
                f"Mesa ID: {pedido['mesa_id']}"
            )
        print()
    else:
        print("\nError al listar pedidos.\n")


def obtener_pedido():
   
    pedido_id = input("Ingrese el ID del pedido: ")
    respuesta = requests.get(f"{BASE_URL}{pedido_id}")

    if respuesta.status_code == 200:
        pedido = respuesta.json()
        print("\n--- PEDIDO ENCONTRADO ---")
        print(f"ID: {pedido['id']}")
        print(f"Estado: {pedido['estado']}")
        print(f"Fecha: {pedido['fecha']}")
        print(f"Cliente ID: {pedido['cliente_id']}")
        print(f"Empleado ID: {pedido['empleado_id']}")
        print(f"Mesa ID: {pedido['mesa_id']}\n")
    else:
        print("\nPedido no encontrado.\n")


def crear_pedido():
    
    estado = input("Ingrese el estado: ")
    cliente_id = int(input("Ingrese el ID del cliente: "))
    empleado_id = int(input("Ingrese el ID del empleado: "))
    mesa_id = int(input("Ingrese el ID de la mesa: "))

    datos = {
        "estado": estado,
        "cliente_id": cliente_id,
        "empleado_id": empleado_id,
        "mesa_id": mesa_id
    }

    respuesta = requests.post(BASE_URL, json=datos)

    if respuesta.status_code == 201:
        pedido = respuesta.json()
        print("\nPedido creado correctamente.")
        print(f"ID asignado: {pedido['id']}\n")
    else:
        print("\nError al crear pedido.")
        print(respuesta.text)
        print()


def actualizar_pedido():
   
    pedido_id = input("Ingrese el ID del pedido a actualizar: ")
    estado = input("Nuevo estado (deje vacío si no desea cambiarlo): ")
    cliente_id = input("Nuevo ID del cliente (deje vacío si no desea cambiarlo): ")
    empleado_id = input("Nuevo ID del empleado (deje vacío si no desea cambiarlo): ")
    mesa_id = input("Nuevo ID de la mesa (deje vacío si no desea cambiarlo): ")

    datos = {}

    if estado:
        datos["estado"] = estado
    if cliente_id:
        datos["cliente_id"] = int(cliente_id)
    if empleado_id:
        datos["empleado_id"] = int(empleado_id)
    if mesa_id:
        datos["mesa_id"] = int(mesa_id)

    respuesta = requests.put(f"{BASE_URL}{pedido_id}", json=datos)

    if respuesta.status_code == 200:
        print("\nPedido actualizado correctamente.\n")
    else:
        print("\nError al actualizar pedido.\n")


def eliminar_pedido():
   
    pedido_id = input("Ingrese el ID del pedido a eliminar: ")
    respuesta = requests.delete(f"{BASE_URL}{pedido_id}")

    if respuesta.status_code == 200:
        print("\nPedido eliminado correctamente.\n")
    else:
        print("\nError al eliminar pedido.\n")
import requests

BASE_URL = "http://127.0.0.1:8000/pagos/"


def listar_pagos():
   
    respuesta = requests.get(BASE_URL)

    if respuesta.status_code == 200:
        pagos = respuesta.json()

        if not pagos:
            print("\nNo hay pagos registrados.\n")
            return

        print("\n--- LISTA DE PAGOS ---")
        for pago in pagos:
            print(
                f"ID: {pago['id']} | "
                f"Metodo: {pago['metodo_pago']} | "
                f"Total: {pago['total']} | "
                f"Fecha: {pago['fecha_pago']} | "
                f"Pedido ID: {pago['pedido_id']}"
            )
        print()
    else:
        print("\nError al listar pagos.\n")


def obtener_pago():
    
    pago_id = input("Ingrese el ID del pago: ")
    respuesta = requests.get(f"{BASE_URL}{pago_id}")

    if respuesta.status_code == 200:
        pago = respuesta.json()
        print("\n--- PAGO ENCONTRADO ---")
        print(f"ID: {pago['id']}")
        print(f"Metodo: {pago['metodo_pago']}")
        print(f"Total: {pago['total']}")
        print(f"Fecha: {pago['fecha_pago']}")
        print(f"Pedido ID: {pago['pedido_id']}\n")
    else:
        print("\nPago no encontrado.\n")


def crear_pago():
   
    metodo_pago = input("Ingrese el metodo de pago: ")
    total = float(input("Ingrese el total: "))
    pedido_id = int(input("Ingrese el ID del pedido: "))

    datos = {
        "metodo_pago": metodo_pago,
        "total": total,
        "pedido_id": pedido_id
    }

    respuesta = requests.post(BASE_URL, json=datos)

    if respuesta.status_code == 201:
        pago = respuesta.json()
        print("\nPago creado correctamente.")
        print(f"ID asignado: {pago['id']}\n")
    else:
        print("\nError al crear pago.")
        print(respuesta.text)
        print()


def actualizar_pago():
    
    pago_id = input("Ingrese el ID del pago a actualizar: ")
    metodo_pago = input("Nuevo metodo de pago (deje vacío si no desea cambiarlo): ")
    total = input("Nuevo total (deje vacío si no desea cambiarlo): ")
    pedido_id = input("Nuevo ID del pedido (deje vacío si no desea cambiarlo): ")

    datos = {}

    if metodo_pago:
        datos["metodo_pago"] = metodo_pago
    if total:
        datos["total"] = float(total)
    if pedido_id:
        datos["pedido_id"] = int(pedido_id)

    respuesta = requests.put(f"{BASE_URL}{pago_id}", json=datos)

    if respuesta.status_code == 200:
        print("\nPago actualizado correctamente.\n")
    else:
        print("\nError al actualizar pago.\n")


def eliminar_pago():
   
    pago_id = input("Ingrese el ID del pago a eliminar: ")
    respuesta = requests.delete(f"{BASE_URL}{pago_id}")

    if respuesta.status_code == 200:
        print("\nPago eliminado correctamente.\n")
    else:
        print("\nError al eliminar pago.\n")
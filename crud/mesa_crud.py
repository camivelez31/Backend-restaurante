import requests

BASE_URL = "http://127.0.0.1:8000/mesas/"


def listar_mesas():
  
    respuesta = requests.get(BASE_URL)

    if respuesta.status_code == 200:
        mesas = respuesta.json()

        if not mesas:
            print("\nNo hay mesas registradas.\n")
            return

        print("\n--- LISTA DE MESAS ---")
        for mesa in mesas:
            print(
                f"ID: {mesa['id']} | "
                f"Numero: {mesa['numero_mesa']} | "
                f"Capacidad: {mesa['capacidad']} | "
                f"Estado: {mesa['estado']}"
            )
        print()
    else:
        print("\nError al listar mesas.\n")


def obtener_mesa():
    
    mesa_id = input("Ingrese el ID de la mesa: ")
    respuesta = requests.get(f"{BASE_URL}{mesa_id}")

    if respuesta.status_code == 200:
        mesa = respuesta.json()
        print("\n--- MESA ENCONTRADA ---")
        print(f"ID: {mesa['id']}")
        print(f"Numero: {mesa['numero_mesa']}")
        print(f"Capacidad: {mesa['capacidad']}")
        print(f"Estado: {mesa['estado']}\n")
    else:
        print("\nMesa no encontrada.\n")


def crear_mesa():
   
    numero_mesa = int(input("Ingrese el numero de mesa: "))
    capacidad = int(input("Ingrese la capacidad: "))
    estado = input("Ingrese el estado: ")

    datos = {
        "numero_mesa": numero_mesa,
        "capacidad": capacidad,
        "estado": estado
    }

    respuesta = requests.post(BASE_URL, json=datos)

    if respuesta.status_code == 201:
        mesa = respuesta.json()
        print("\nMesa creada correctamente.")
        print(f"ID asignado: {mesa['id']}\n")
    else:
        print("\nError al crear mesa.")
        print(respuesta.text)
        print()


def actualizar_mesa():
    
    mesa_id = input("Ingrese el ID de la mesa a actualizar: ")
    numero_mesa = input("Nuevo numero de mesa (deje vacío si no desea cambiarlo): ")
    capacidad = input("Nueva capacidad (deje vacío si no desea cambiarlo): ")
    estado = input("Nuevo estado (deje vacío si no desea cambiarlo): ")

    datos = {}

    if numero_mesa:
        datos["numero_mesa"] = int(numero_mesa)
    if capacidad:
        datos["capacidad"] = int(capacidad)
    if estado:
        datos["estado"] = estado

    respuesta = requests.put(f"{BASE_URL}{mesa_id}", json=datos)

    if respuesta.status_code == 200:
        print("\nMesa actualizada correctamente.\n")
    else:
        print("\nError al actualizar mesa.\n")


def eliminar_mesa():
    
    mesa_id = input("Ingrese el ID de la mesa a eliminar: ")
    respuesta = requests.delete(f"{BASE_URL}{mesa_id}")

    if respuesta.status_code == 200:
        print("\nMesa eliminada correctamente.\n")
    else:
        print("\nError al eliminar mesa.\n")
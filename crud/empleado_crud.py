import requests

BASE_URL = "http://127.0.0.1:8000/empleados/"


def listar_empleados():
  
    respuesta = requests.get(BASE_URL)

    if respuesta.status_code == 200:
        empleados = respuesta.json()

        if not empleados:
            print("\nNo hay empleados registrados.\n")
            return

        print("\n--- LISTA DE EMPLEADOS ---")
        for empleado in empleados:
            print(
                f"ID: {empleado['id']} | "
                f"Nombre: {empleado['nombre']} | "
                f"Cargo: {empleado['cargo']} | "
                f"Telefono: {empleado['telefono']}"
            )
        print()
    else:
        print("\nError al listar empleados.\n")


def obtener_empleado():
  
    empleado_id = input("Ingrese el ID del empleado: ")

    respuesta = requests.get(f"{BASE_URL}{empleado_id}")

    if respuesta.status_code == 200:
        empleado = respuesta.json()
        print("\n--- EMPLEADO ENCONTRADO ---")
        print(f"ID: {empleado['id']}")
        print(f"Nombre: {empleado['nombre']}")
        print(f"Cargo: {empleado['cargo']}")
        print(f"Telefono: {empleado['telefono']}\n")
    else:
        print("\nEmpleado no encontrado.\n")


def crear_empleado():
   
    nombre = input("Ingrese el nombre: ")
    cargo = input("Ingrese el cargo: ")
    telefono = input("Ingrese el telefono: ")

    datos = {
        "nombre": nombre,
        "cargo": cargo,
        "telefono": telefono
    }

    respuesta = requests.post(BASE_URL, json=datos)

    if respuesta.status_code == 201:
        empleado = respuesta.json()
        print("\nEmpleado creado correctamente.")
        print(f"ID asignado: {empleado['id']}\n")
    else:
        print("\nError al crear empleado.")
        print(respuesta.text)
        print()


def actualizar_empleado():
   
    empleado_id = input("Ingrese el ID del empleado a actualizar: ")
    nombre = input("Nuevo nombre (deje vacío si no desea cambiarlo): ")
    cargo = input("Nuevo cargo (deje vacío si no desea cambiarlo): ")
    telefono = input("Nuevo telefono (deje vacío si no desea cambiarlo): ")

    datos = {}

    if nombre:
        datos["nombre"] = nombre
    if cargo:
        datos["cargo"] = cargo
    if telefono:
        datos["telefono"] = telefono

    respuesta = requests.put(f"{BASE_URL}{empleado_id}", json=datos)

    if respuesta.status_code == 200:
        print("\nEmpleado actualizado correctamente.\n")
    else:
        print("\nError al actualizar empleado.\n")


def eliminar_empleado():
   
    empleado_id = input("Ingrese el ID del empleado a eliminar: ")

    respuesta = requests.delete(f"{BASE_URL}{empleado_id}")

    if respuesta.status_code == 200:
        print("\nEmpleado eliminado correctamente.\n")
    else:
        print("\nError al eliminar empleado.\n")
import requests

BASE_URL = "http://127.0.0.1:8000/platos/"


def listar_platos():
  
    respuesta = requests.get(BASE_URL)

    if respuesta.status_code == 200:
        platos = respuesta.json()

        if not platos:
            print("\nNo hay platos registrados.\n")
            return

        print("\n--- LISTA DE PLATOS ---")
        for plato in platos:
            print(
                f"ID: {plato['id']} | "
                f"Nombre: {plato['nombre']} | "
                f"Precio: {plato['precio']} | "
                f"Disponible: {plato['disponible']} | "
                f"Categoria ID: {plato['categoria_id']}"
            )
        print()
    else:
        print("\nError al listar platos.\n")


def obtener_plato():
   
    plato_id = input("Ingrese el ID del plato: ")
    respuesta = requests.get(f"{BASE_URL}{plato_id}")

    if respuesta.status_code == 200:
        plato = respuesta.json()
        print("\n--- PLATO ENCONTRADO ---")
        print(f"ID: {plato['id']}")
        print(f"Nombre: {plato['nombre']}")
        print(f"Descripcion: {plato['descripcion']}")
        print(f"Precio: {plato['precio']}")
        print(f"Disponible: {plato['disponible']}")
        print(f"Categoria ID: {plato['categoria_id']}\n")
    else:
        print("\nPlato no encontrado.\n")


def crear_plato():
   
    nombre = input("Ingrese el nombre: ")
    descripcion = input("Ingrese la descripcion: ")
    precio = float(input("Ingrese el precio: "))
    disponible = input("¿Está disponible? (true/false): ").lower() == "true"
    categoria_id = int(input("Ingrese el ID de la categoria: "))

    datos = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "disponible": disponible,
        "categoria_id": categoria_id
    }

    respuesta = requests.post(BASE_URL, json=datos)

    if respuesta.status_code == 201:
        plato = respuesta.json()
        print("\nPlato creado correctamente.")
        print(f"ID asignado: {plato['id']}\n")
    else:
        print("\nError al crear plato.")
        print(respuesta.text)
        print()


def actualizar_plato():
  
    plato_id = input("Ingrese el ID del plato a actualizar: ")
    nombre = input("Nuevo nombre (deje vacío si no desea cambiarlo): ")
    descripcion = input("Nueva descripcion (deje vacío si no desea cambiarla): ")
    precio = input("Nuevo precio (deje vacío si no desea cambiarlo): ")
    disponible = input("Nuevo disponible (true/false, deje vacío si no desea cambiarlo): ")
    categoria_id = input("Nuevo ID de categoria (deje vacío si no desea cambiarlo): ")

    datos = {}

    if nombre:
        datos["nombre"] = nombre
    if descripcion:
        datos["descripcion"] = descripcion
    if precio:
        datos["precio"] = float(precio)
    if disponible:
        datos["disponible"] = disponible.lower() == "true"
    if categoria_id:
        datos["categoria_id"] = int(categoria_id)

    respuesta = requests.put(f"{BASE_URL}{plato_id}", json=datos)

    if respuesta.status_code == 200:
        print("\nPlato actualizado correctamente.\n")
    else:
        print("\nError al actualizar plato.\n")


def eliminar_plato():
  
    plato_id = input("Ingrese el ID del plato a eliminar: ")
    respuesta = requests.delete(f"{BASE_URL}{plato_id}")

    if respuesta.status_code == 200:
        print("\nPlato eliminado correctamente.\n")
    else:
        print("\nError al eliminar plato.\n")
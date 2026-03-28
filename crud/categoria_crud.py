import requests

BASE_URL = "http://127.0.0.1:8000/categorias/"


def listar_categorias():
 
    respuesta = requests.get(BASE_URL)

    if respuesta.status_code == 200:
        categorias = respuesta.json()

        if not categorias:
            print("\nNo hay categorias registradas.\n")
            return

        print("\n--- LISTA DE CATEGORIAS ---")
        for categoria in categorias:
            print(
                f"ID: {categoria['id']} | "
                f"Nombre: {categoria['nombre']} | "
                f"Descripcion: {categoria['descripcion']}"
            )
        print()
    else:
        print("\nError al listar categorias.\n")


def obtener_categoria():
  
    categoria_id = input("Ingrese el ID de la categoria: ")
    respuesta = requests.get(f"{BASE_URL}{categoria_id}")

    if respuesta.status_code == 200:
        categoria = respuesta.json()
        print("\n--- CATEGORIA ENCONTRADA ---")
        print(f"ID: {categoria['id']}")
        print(f"Nombre: {categoria['nombre']}")
        print(f"Descripcion: {categoria['descripcion']}\n")
    else:
        print("\nCategoria no encontrada.\n")


def crear_categoria():
   
    nombre = input("Ingrese el nombre: ")
    descripcion = input("Ingrese la descripcion: ")

    datos = {
        "nombre": nombre,
        "descripcion": descripcion
    }

    respuesta = requests.post(BASE_URL, json=datos)

    if respuesta.status_code == 201:
        categoria = respuesta.json()
        print("\nCategoria creada correctamente.")
        print(f"ID asignado: {categoria['id']}\n")
    else:
        print("\nError al crear categoria.")
        print(respuesta.text)
        print()


def actualizar_categoria():
    
    categoria_id = input("Ingrese el ID de la categoria a actualizar: ")
    nombre = input("Nuevo nombre (deje vacío si no desea cambiarlo): ")
    descripcion = input("Nueva descripcion (deje vacío si no desea cambiarla): ")

    datos = {}

    if nombre:
        datos["nombre"] = nombre
    if descripcion:
        datos["descripcion"] = descripcion

    respuesta = requests.put(f"{BASE_URL}{categoria_id}", json=datos)

    if respuesta.status_code == 200:
        print("\nCategoria actualizada correctamente.\n")
    else:
        print("\nError al actualizar categoria.\n")


def eliminar_categoria():
 
    categoria_id = input("Ingrese el ID de la categoria a eliminar: ")
    respuesta = requests.delete(f"{BASE_URL}{categoria_id}")

    if respuesta.status_code == 200:
        print("\nCategoria eliminada correctamente.\n")
    else:
        print("\nError al eliminar categoria.\n")
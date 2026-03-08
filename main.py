print("Se esta ejecutando main.py")

from crud.cliente_crud import (
    listar_clientes,
    obtener_cliente,
    crear_cliente,
    actualizar_cliente,
    eliminar_cliente
)

from crud.empleado_crud import (
    listar_empleados,
    obtener_empleado,
    crear_empleado,
    actualizar_empleado,
    eliminar_empleado
)


def menu_clientes():
   
    while True:
        print("\n--- MENU CLIENTES ---")
        print("1. Listar clientes")
        print("2. Obtener cliente por ID")
        print("3. Crear cliente")
        print("4. Actualizar cliente")
        print("5. Eliminar cliente")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            listar_clientes()
        elif opcion == "2":
            obtener_cliente()
        elif opcion == "3":
            crear_cliente()
        elif opcion == "4":
            actualizar_cliente()
        elif opcion == "5":
            eliminar_cliente()
        elif opcion == "6":
            break
        else:
            print("\nOpcion no valida.\n")


def menu_empleados():
    
    while True:
        print("\n--- MENU EMPLEADOS ---")
        print("1. Listar empleados")
        print("2. Obtener empleado por ID")
        print("3. Crear empleado")
        print("4. Actualizar empleado")
        print("5. Eliminar empleado")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            listar_empleados()
        elif opcion == "2":
            obtener_empleado()
        elif opcion == "3":
            crear_empleado()
        elif opcion == "4":
            actualizar_empleado()
        elif opcion == "5":
            eliminar_empleado()
        elif opcion == "6":
            break
        else:
            print("\nOpcion no valida.\n")


def main():
 
    while True:
        print("\n=== SISTEMA DE RESTAURANTE ===")
        print("1. Gestionar clientes")
        print("2. Gestionar empleados")
        print("3. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_empleados()
        elif opcion == "3":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpcion no valida.\n")


if __name__ == "__main__":
    main()
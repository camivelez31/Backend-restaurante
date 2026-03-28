
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

from crud.mesa_crud import (
    listar_mesas,
    obtener_mesa,
    crear_mesa,
    actualizar_mesa,
    eliminar_mesa
)

from crud.categoria_crud import (
    listar_categorias,
    obtener_categoria,
    crear_categoria,
    actualizar_categoria,
    eliminar_categoria
)

from crud.plato_crud import (
    listar_platos,
    obtener_plato,
    crear_plato,
    actualizar_plato,
    eliminar_plato
)

from crud.pedido_crud import (
    listar_pedidos,
    obtener_pedido,
    crear_pedido,
    actualizar_pedido,
    eliminar_pedido
)

from crud.pago_crud import (
    listar_pagos,
    obtener_pago,
    crear_pago,
    actualizar_pago,
    eliminar_pago
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


def menu_mesas():
  
    while True:
        print("\n--- MENU MESAS ---")
        print("1. Listar mesas")
        print("2. Obtener mesa por ID")
        print("3. Crear mesa")
        print("4. Actualizar mesa")
        print("5. Eliminar mesa")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            listar_mesas()
        elif opcion == "2":
            obtener_mesa()
        elif opcion == "3":
            crear_mesa()
        elif opcion == "4":
            actualizar_mesa()
        elif opcion == "5":
            eliminar_mesa()
        elif opcion == "6":
            break
        else:
            print("\nOpcion no valida.\n")


def menu_categorias():
   
    while True:
        print("\n--- MENU CATEGORIAS ---")
        print("1. Listar categorias")
        print("2. Obtener categoria por ID")
        print("3. Crear categoria")
        print("4. Actualizar categoria")
        print("5. Eliminar categoria")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            listar_categorias()
        elif opcion == "2":
            obtener_categoria()
        elif opcion == "3":
            crear_categoria()
        elif opcion == "4":
            actualizar_categoria()
        elif opcion == "5":
            eliminar_categoria()
        elif opcion == "6":
            break
        else:
            print("\nOpcion no valida.\n")


def menu_platos():
    
    while True:
        print("\n--- MENU PLATOS ---")
        print("1. Listar platos")
        print("2. Obtener plato por ID")
        print("3. Crear plato")
        print("4. Actualizar plato")
        print("5. Eliminar plato")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            listar_platos()
        elif opcion == "2":
            obtener_plato()
        elif opcion == "3":
            crear_plato()
        elif opcion == "4":
            actualizar_plato()
        elif opcion == "5":
            eliminar_plato()
        elif opcion == "6":
            break
        else:
            print("\nOpcion no valida.\n")


def menu_pedidos():
   
    while True:
        print("\n--- MENU PEDIDOS ---")
        print("1. Listar pedidos")
        print("2. Obtener pedido por ID")
        print("3. Crear pedido")
        print("4. Actualizar pedido")
        print("5. Eliminar pedido")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            listar_pedidos()
        elif opcion == "2":
            obtener_pedido()
        elif opcion == "3":
            crear_pedido()
        elif opcion == "4":
            actualizar_pedido()
        elif opcion == "5":
            eliminar_pedido()
        elif opcion == "6":
            break
        else:
            print("\nOpcion no valida.\n")


def menu_pagos():
    
    while True:
        print("\n--- MENU PAGOS ---")
        print("1. Listar pagos")
        print("2. Obtener pago por ID")
        print("3. Crear pago")
        print("4. Actualizar pago")
        print("5. Eliminar pago")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            listar_pagos()
        elif opcion == "2":
            obtener_pago()
        elif opcion == "3":
            crear_pago()
        elif opcion == "4":
            actualizar_pago()
        elif opcion == "5":
            eliminar_pago()
        elif opcion == "6":
            break
        else:
            print("\nOpcion no valida.\n")


def main():
  
    while True:
        print("\n=== SISTEMA DE RESTAURANTE ===")
        print("1. Gestionar clientes")
        print("2. Gestionar empleados")
        print("3. Gestionar mesas")
        print("4. Gestionar categorias")
        print("5. Gestionar platos")
        print("6. Gestionar pedidos")
        print("7. Gestionar pagos")
        print("8. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_empleados()
        elif opcion == "3":
            menu_mesas()
        elif opcion == "4":
            menu_categorias()
        elif opcion == "5":
            menu_platos()
        elif opcion == "6":
            menu_pedidos()
        elif opcion == "7":
            menu_pagos()
        elif opcion == "8":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpcion no valida.\n")


if __name__ == "__main__":
    main()
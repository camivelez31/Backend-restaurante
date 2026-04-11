from database.connection import SessionLocal
from entities.categoria import Categoria
from entities.clientes import Cliente
from entities.empleado import Empleado
from entities.mesa import Mesa


def seed_categorias(db):
    """
     categorías iniciales si no existen.
    """
    categorias = [
        {"nombre": "Entradas", "descripcion": "Platos para iniciar la comida"},
        {"nombre": "Platos fuertes", "descripcion": "Platos principales"},
        {"nombre": "Bebidas", "descripcion": "Jugos, gaseosas y bebidas"},
        {"nombre": "Postres", "descripcion": "Postres y dulces"}
    ]

    for categoria in categorias:
        existente = db.query(Categoria).filter(
            Categoria.nombre == categoria["nombre"]
        ).first()

        if not existente:
            nueva_categoria = Categoria(
                nombre=categoria["nombre"],
                descripcion=categoria["descripcion"]
            )
            db.add(nueva_categoria)


def seed_mesas(db):
    """
     mesas iniciales si no existen.
    """
    mesas = [
        {"numero_mesa": 1, "capacidad": 4, "estado": "disponible"},
        {"numero_mesa": 2, "capacidad": 2, "estado": "disponible"},
        {"numero_mesa": 3, "capacidad": 6, "estado": "ocupada"}
    ]

    for mesa in mesas:
        existente = db.query(Mesa).filter(
            Mesa.numero_mesa == mesa["numero_mesa"]
        ).first()

        if not existente:
            nueva_mesa = Mesa(
                numero_mesa=mesa["numero_mesa"],
                capacidad=mesa["capacidad"],
                estado=mesa["estado"]
            )
            db.add(nueva_mesa)


def seed_cliente_inicial(db):
    """
    Inserta un cliente inicial si no existe.
    """
    existente = db.query(Cliente).filter(
        Cliente.correo == "clienteinicial@gmail.com"
    ).first()

    if not existente:
        nuevo_cliente = Cliente(
            nombre="Cliente Inicial",
            telefono="3000000001",
            correo="clienteinicial@gmail.com"
        )
        db.add(nuevo_cliente)


def seed_empleado_inicial(db):
    """
    Inserta un empleado inicial si no existe.
    """
    existente = db.query(Empleado).filter(
        Empleado.telefono == "3000000002"
    ).first()

    if not existente:
        nuevo_empleado = Empleado(
            nombre="Empleado Inicial",
            cargo="Administrador",
            telefono="3000000002"
        )
        db.add(nuevo_empleado)


def run_seed():
    """
    Ejecuta el seeder general.
    """
    db = SessionLocal()

    try:
        seed_categorias(db)
        seed_mesas(db)
        seed_cliente_inicial(db)
        seed_empleado_inicial(db)

        db.commit()
        print("Seeder ejecutado correctamente.")
    except Exception as error:
        db.rollback()
        print("Error al ejecutar el seeder:")
        print(error)
    finally:
        db.close()
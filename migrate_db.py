from database.base import Base
from database.connection import engine
import entities


def migrate_database():
    """
    Ejecuta la actualización del esquema de base de datos.
    """
    Base.metadata.create_all(bind=engine)
    print("Base de datos actualizada correctamente.")


if __name__ == "__main__":
    migrate_database()
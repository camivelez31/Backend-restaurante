from database.base import Base
from database.connection import engine
import entities


def create_tables():
   
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas en la base de datos Neon")


if __name__ == "__main__":
    create_tables()
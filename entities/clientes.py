from sqlalchemy import Column, Integer, String
from database.base import Base


class Cliente(Base):
   

    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(20), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
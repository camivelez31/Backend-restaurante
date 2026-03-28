from sqlalchemy import Column, Integer, String
from database.base import Base


class Empleado(Base):

    __tablename__ = "empleados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    cargo = Column(String(50), nullable=False)
    telefono = Column(String(20), nullable=False)
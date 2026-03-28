from sqlalchemy import Column, Integer, String
from database.base import Base


class Mesa(Base):


    __tablename__ = "mesas"

    id = Column(Integer, primary_key=True, index=True)
    numero_mesa = Column(Integer, unique=True, nullable=False)
    capacidad = Column(Integer, nullable=False)
    estado = Column(String(30), nullable=False)
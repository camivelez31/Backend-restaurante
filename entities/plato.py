from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from database.base import Base


class Plato(Base):


    __tablename__ = "platos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)
    precio = Column(Float, nullable=False)
    disponible = Column(Boolean, default=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
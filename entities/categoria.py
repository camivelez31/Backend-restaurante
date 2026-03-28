from sqlalchemy import Column, Integer, String
from database.base import Base


class Categoria(Base):
   

    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(String(255), nullable=True)
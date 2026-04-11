from sqlalchemy import Column, Integer, String
from database.base import Base


class Usuario(Base):
    """
     usuarios autenticables del sistema.
    """

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
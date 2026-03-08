from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from datetime import datetime
from database.base import Base


class Pedido(Base):
  
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    estado = Column(String(50), nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    empleado_id = Column(Integer, ForeignKey("empleados.id"), nullable=False)
    mesa_id = Column(Integer, ForeignKey("mesas.id"), nullable=False)
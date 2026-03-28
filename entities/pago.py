from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from datetime import datetime
from database.base import Base


class Pago(Base):


    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    metodo_pago = Column(String(50), nullable=False)
    total = Column(Float, nullable=False)
    fecha_pago = Column(DateTime, default=datetime.utcnow)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
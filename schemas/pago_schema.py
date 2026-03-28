from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class PagoBase(BaseModel):
  

    metodo_pago: str
    total: float
    pedido_id: int


class PagoCreate(PagoBase):
 
    pass


class PagoUpdate(BaseModel):
    

    metodo_pago: Optional[str] = None
    total: Optional[float] = None
    pedido_id: Optional[int] = None


class PagoResponse(PagoBase):
  

    id: int
    fecha_pago: datetime

    class Config:
        from_attributes = True
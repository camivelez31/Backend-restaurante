from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class PedidoBase(BaseModel):
   

    estado: str
    cliente_id: int
    empleado_id: int
    mesa_id: int


class PedidoCreate(PedidoBase):

    pass


class PedidoUpdate(BaseModel):


    estado: Optional[str] = None
    cliente_id: Optional[int] = None
    empleado_id: Optional[int] = None
    mesa_id: Optional[int] = None


class PedidoResponse(PedidoBase):
   

    id: int
    fecha: datetime

    class Config:
        from_attributes = True
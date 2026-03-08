from pydantic import BaseModel
from typing import Optional


class MesaBase(BaseModel):
 

    numero_mesa: int
    capacidad: int
    estado: str


class MesaCreate(MesaBase):
   
    pass


class MesaUpdate(BaseModel):
  

    numero_mesa: Optional[int] = None
    capacidad: Optional[int] = None
    estado: Optional[str] = None


class MesaResponse(MesaBase):
   

    id: int

    class Config:
        from_attributes = True
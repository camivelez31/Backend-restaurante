from pydantic import BaseModel
from typing import Optional


class PlatoBase(BaseModel):
   
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    disponible: bool = True
    categoria_id: int


class PlatoCreate(PlatoBase):
  
    pass


class PlatoUpdate(BaseModel):
 

    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    disponible: Optional[bool] = None
    categoria_id: Optional[int] = None


class PlatoResponse(PlatoBase):


    id: int

    class Config:
        from_attributes = True
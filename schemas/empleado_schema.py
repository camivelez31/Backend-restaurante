from pydantic import BaseModel
from typing import Optional


class EmpleadoBase(BaseModel):
  

    nombre: str
    cargo: str
    telefono: str


class EmpleadoCreate(EmpleadoBase):
   
    pass


class EmpleadoUpdate(BaseModel):
   

    nombre: Optional[str] = None
    cargo: Optional[str] = None
    telefono: Optional[str] = None


class EmpleadoResponse(EmpleadoBase):
   

    id: int

    class Config:
        from_attributes = True
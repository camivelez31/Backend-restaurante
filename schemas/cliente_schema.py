from pydantic import BaseModel, EmailStr
from typing import Optional


class ClienteBase(BaseModel):
    """
    Schema base para los datos de un cliente.
    """

    nombre: str
    telefono: str
    correo: EmailStr


class ClienteCreate(ClienteBase):
  
    pass


class ClienteUpdate(BaseModel):
 

    nombre: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[EmailStr] = None


class ClienteResponse(ClienteBase):
 

    id: int

    class Config:
        from_attributes = True
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from core.exceptions import BadRequestException
from database.connection import get_db
from entities.usuario import Usuario
from utils.security import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Usuario:
    """
    Obtiene el usuario autenticado a partir del token JWT.
    """
    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")

        if username is None:
            raise BadRequestException("Token inválido")
    except JWTError:
        raise BadRequestException("Token inválido o expirado")

    usuario = db.query(Usuario).filter(Usuario.username == username).first()

    if not usuario:
        raise BadRequestException("Usuario no encontrado")

    return usuario
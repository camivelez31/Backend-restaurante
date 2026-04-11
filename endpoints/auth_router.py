from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core.exceptions import BadRequestException
from database.connection import get_db
from entities.usuario import Usuario
from schemas.auth_schema import Token
from utils.security import create_access_token, verify_password

router = APIRouter(prefix="/auth", tags=["Autenticacion"])


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Realiza login y retorna un JWT si las credenciales son válidas.
    """
    usuario = db.query(Usuario).filter(Usuario.username == form_data.username).first()

    if not usuario:
        raise BadRequestException("Credenciales inválidas")

    if not verify_password(form_data.password, usuario.hashed_password):
        raise BadRequestException("Credenciales inválidas")

    access_token = create_access_token(
        data={"sub": usuario.username},
        expires_delta=timedelta(minutes=60)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
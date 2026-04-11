from pydantic import BaseModel


class Token(BaseModel):
    """
    Schema de respuesta para el token JWT.
    """

    access_token: str
    token_type: str


class LoginData(BaseModel):
    """
    Schema para login manual si luego lo necesitas.
    """

    username: str
    password: str
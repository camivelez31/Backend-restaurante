def error_response(status_code: int, message: str, detail: str = None) -> dict:
    """
    respuesta de error homogénea.
    """
    return {
        "status_code": status_code,
        "message": message,
        "detail": detail
    }
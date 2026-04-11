class AppException(Exception):
    """
    Excepción base de la aplicación.
    """

    def __init__(self, status_code: int, message: str, detail: str = None):
        self.status_code = status_code
        self.message = message
        self.detail = detail
        super().__init__(message)


class NotFoundException(AppException):

    def __init__(self, detail: str = "Recurso no encontrado"):
        super().__init__(404, "Not Found", detail)


class BadRequestException(AppException):

    def __init__(self, detail: str = "Solicitud inválida"):
        super().__init__(400, "Bad Request", detail)


class ConflictException(AppException):

    def __init__(self, detail: str = "Conflicto de datos"):
        super().__init__(409, "Conflict", detail)
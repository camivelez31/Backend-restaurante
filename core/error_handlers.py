from fastapi import Request
from fastapi.responses import JSONResponse

from core.exceptions import AppException
from core.responses import error_response


async def app_exception_handler(request: Request, exc: AppException):
    """
   excepciones personalizadas de la aplicación.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(
            status_code=exc.status_code,
            message=exc.message,
            detail=exc.detail
        )
    )


async def generic_exception_handler(request: Request, exc: Exception):
    """
    excepciones no controladas.
    """
    return JSONResponse(
        status_code=500,
        content=error_response(
            status_code=500,
            message="Internal Server Error",
            detail=str(exc)
        )
    )
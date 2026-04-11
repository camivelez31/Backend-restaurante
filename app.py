from fastapi import FastAPI

from core.error_handlers import app_exception_handler, generic_exception_handler
from core.exceptions import AppException

from endpoints.categoria_router import router as categoria_router
from endpoints.cliente_router import router as cliente_router
from endpoints.empleado_router import router as empleado_router
from endpoints.mesa_router import router as mesa_router
from endpoints.pago_router import router as pago_router
from endpoints.pedido_router import router as pedido_router
from endpoints.plato_router import router as plato_router
from endpoints.auth_router import router as auth_router

app = FastAPI(
    title="API REST Restaurante",
    description="API para la gestion de un sistema de restaurante",
    version="1.0.0"
)

app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(cliente_router)
app.include_router(empleado_router)
app.include_router(mesa_router)
app.include_router(categoria_router)
app.include_router(plato_router)
app.include_router(pedido_router)
app.include_router(pago_router)
app.include_router(auth_router)
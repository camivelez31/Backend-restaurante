# BACKEND-Restaurante

Sistema de restaurante desarrollado para gestionar el funcionamiento básico de un establecimiento, permitiendo la administración de clientes, empleados, mesas, platos, pedidos y pagos.

## Sistema de Restaurante – API REST con FastAPI

### Descripción

Este proyecto implementa una **API REST** utilizando **FastAPI** para gestionar un sistema de restaurante.

La aplicación permite realizar operaciones CRUD (**Crear, Leer, Actualizar, Eliminar**) sobre las diferentes entidades del sistema mediante endpoints HTTP.

El proyecto utiliza:

* **FastAPI** para la API
* **PostgreSQL (Neon)** como base de datos
* **SQLAlchemy** como ORM
* **Pydantic** para validación de datos
* **Uvicorn** como servidor ASGI
* **Requests** para el cliente HTTP del menú por consola

Además, incluye un **menú por consola** que consume la API mediante peticiones HTTP.

### Tecnologías utilizadas

* Python 3.10+
* FastAPI
* Uvicorn
* PostgreSQL (Neon)
* SQLAlchemy
* Pydantic
* Requests
* python-dotenv

### Arquitectura del proyecto

El proyecto sigue una arquitectura modular separando responsabilidades por capas.

```bash
Backend-restaurante/
│
├── app.py                       # Aplicación FastAPI y registro de routers
│
├── database/                    # Conexión a PostgreSQL
│   ├── base.py
│   └── connection.py
│
├── entities/                    # Modelos ORM (SQLAlchemy)
│   ├── cliente.py
│   ├── empleado.py
│   ├── mesa.py
│   ├── categoria.py
│   ├── plato.py
│   ├── pedido.py
│   └── pago.py
│
├── schemas/                     # Modelos Pydantic
│   ├── cliente_schema.py
│   ├── empleado_schema.py
│   ├── mesa_schema.py
│   ├── categoria_schema.py
│   ├── plato_schema.py
│   ├── pedido_schema.py
│   └── pago_schema.py
│
├── endpoints/                   # Rutas FastAPI
│   ├── clientes_router.py
│   ├── empleados_router.py
│   ├── mesas_router.py
│   ├── categorias_router.py
│   ├── platos_router.py
│   ├── pedidos_router.py
│   └── pagos_router.py
│
├── crud/                        # Cliente HTTP para consumir la API
│   └── crud_client.py
│
├── main.py                      # Menú por consola
├── create_tables.py             # Script para crear tablas
├── test_connection.py           # Script de prueba de conexión
│
├── requirements.txt
└── README.md
```

### Entidades del sistema

El sistema incluye 7 entidades principales:

#### Cliente

Representa a la persona que realiza pedidos en el restaurante.

#### Empleado

Representa al personal encargado de atender y gestionar pedidos.

#### Mesa

Representa las mesas disponibles dentro del restaurante.

#### Categoría

Permite clasificar los platos del menú.

#### Plato

Representa los productos o comidas ofrecidas por el restaurante.

#### Pedido

Representa la orden realizada por un cliente.

#### Pago

Representa el registro del pago asociado a un pedido.

### Relaciones entre entidades

* Un cliente puede tener muchos pedidos
* Un empleado puede gestionar muchos pedidos
* Una mesa puede estar asociada a muchos pedidos
* Una categoría puede tener muchos platos
* Un pedido puede generar un pago

### Instalación

#### 1. Clonar el repositorio

```bash
git clone https://github.com/camivelez31/Backend-restaurante.git
cd Backend-restaurante
```

#### 2. Crear entorno virtual

```bash
python -m venv venv
```


**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

#### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### Configuración de base de datos


```env
DATABASE_URL=postgresql://usuario:password@host/database
```

La base de datos utilizada es **PostgreSQL en Neon**.

### Crear tablas en la base de datos



```bash
python create_tables.py
```


### Ejecutar la API

```bash
uvicorn app:app --reload
```



```bash
http://127.0.0.1:8000
```

### Documentación automática


```bash
http://127.0.0.1:8000/docs
```

### Endpoints principales

#### Clientes

* GET /clientes
* GET /clientes/{id}
* POST /clientes
* PUT /clientes/{id}
* DELETE /clientes/{id}

#### Empleados

* GET /empleados
* GET /empleados/{id}
* POST /empleados
* PUT /empleados/{id}
* DELETE /empleados/{id}

#### Mesas

* GET /mesas
* GET /mesas/{id}
* POST /mesas
* PUT /mesas/{id}
* DELETE /mesas/{id}

#### Categorías

* GET /categorias
* GET /categorias/{id}
* POST /categorias
* PUT /categorias/{id}
* DELETE /categorias/{id}

#### Platos

* GET /platos
* GET /platos/{id}
* POST /platos
* PUT /platos/{id}
* DELETE /platos/{id}

#### Pedidos

* GET /pedidos
* GET /pedidos/{id}
* POST /pedidos
* PUT /pedidos/{id}
* DELETE /pedidos/{id}

#### Pagos

* GET /pagos
* GET /pagos/{id}
* POST /pagos
* PUT /pagos/{id}
* DELETE /pagos/{id}

### Autor

**Maria Camila Vélez Mazo**

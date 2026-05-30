# Backend-restaurante

API REST para un sistema de restaurante desarrollada con FastAPI, SQLAlchemy y PostgreSQL.

---

# Descripción

Proyecto desarrollado para la asignatura Aplicación y Servicios Web.

El sistema permite gestionar diferentes recursos de un restaurante mediante una API REST con autenticación JWT, rutas protegidas y consumo desde frontend web.

---

# Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Neon
- Pydantic
- JWT Authentication

---

# Funcionalidades principales

- CRUD de clientes
- CRUD de empleados
- CRUD de mesas
- CRUD de categorías
- CRUD de platos
- CRUD de pedidos
- CRUD de pagos
- Autenticación JWT
- Rutas protegidas
- Middleware de seguridad
- Configuración CORS

---

# Estructura del proyecto

```bash
Backend-restaurante/
│
├── crud/
├── database/
├── endpoints/
├── entities/
├── schemas/
├── core/
├── .env
├── .gitignore
├── app.py
├── create_tables.py
├── main.py
├── README.md
├── requirements.txt
└── test_connection.py
```

---

# Entidades ORM

El sistema cuenta con ocho entidades ORM:

- Usuarios
- Clientes
- Empleados
- Mesas
- Categorías
- Platos
- Pedidos
- Pagos

---

# Configuración del proyecto

## Clonar repositorio

```bash
git clone https://github.com/camivelez31/Backend-restaurante.git
```

---

## Crear entorno virtual

```bash
python -m venv venv
```

---

## Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución del backend

```bash
uvicorn app:app --reload
```

---

# Swagger

```text
http://127.0.0.1:8000/docs
```

---

# Seguridad implementada

- JWT Authentication
- Authorization Bearer
- Middleware de seguridad
- CORS configurado
- Protección de rutas

---

# Flujo de ramas

El proyecto utiliza flujo de ramas con:

- feat/*
- dev
- qa
- prod

---

# Video de demostración

En el siguiente enlace se muestra:

- Integración backend y frontend
- Login JWT
- Consumo de API REST
- Middleware de seguridad
- CORS
- Rutas protegidas
- Pull Requests
- Pipeline CI/CD
- Seeder y datos de prueba

## Link del video

https://drive.google.com/file/d/10Wsg7wSGalAot8Ugnembom-BAmXsEq9Z/view?usp=sharing

---

# Autor

María Camila Vélez Mazo
Aplicación y Servicios Web - 2026-1
# Backend-restaurante

API REST para un sistema de restaurante desarrollada con FastAPI, Uvicorn y PostgreSQL en Neon.

## Descripción

Este proyecto fue desarrollado para el examen de la asignatura Aplicación y Servicios Web.

El sistema permite gestionar diferentes recursos de un restaurante mediante una API REST y un menú por consola que consume dicha API.

## Funcionalidades

- CRUD de clientes
- CRUD de empleados
- CRUD de mesas
- CRUD de categorias
- CRUD de platos
- CRUD de pedidos
- CRUD de pagos

## Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Neon
- Requests
- Pydantic

## Estructura del proyecto

```bash
Backend-restaurante/
│
├── crud/
├── database/
├── endpoints/
├── entities/
├── schemas/
├── .env
├── .gitignore
├── app.py
├── create_tables.py
├── main.py
├── README.md
├── requirements.txt
└── test_connection.py 
```

```md
## Entidades del sistema

- Clientes
- Empleados
- Mesas
- Categorias
- Platos
- Pedidos
- Pagos


## Flujo de ramas

Se implementa flujo de trabajo con ramas:
- feat/*
- dev
- qa
- prod


##  Video de demostración

En el siguiente enlace se muestra la ejecución del proyecto, incluyendo:

- Pipeline CI/CD
- Autenticación JWT
- Rutas protegidas
- Ejecución de migraciones y seeder

link de video: https://drive.google.com/file/d/10Wsg7wSGalAot8Ugnembom-BAmXsEq9Z/view?usp=sharing
=======

## Flujo de ramas
Este proyecto utiliza ramas dev, feature, qa y prod para control con cambios.



## Autor

Maria Camila Vélez Mazo


















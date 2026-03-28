from database.connection import engine

try:
    connection = engine.connect()
    print("Conexion exitosa con Neon")
    connection.close()
except Exception as error:
    print("Error de conexion:")
    print(error)
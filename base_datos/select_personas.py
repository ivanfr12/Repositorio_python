from conexion import Conexion
from mysql.connector import Error
from mysql.connector import connect

personas_db = connect(
    host="localhost", # 127.0.0.1
    user="root",
    passwd="",
    database="personas_db"
)

# Ejecutar la sentencia select
cursor = personas_db.cursor()
cursor.execute("SELECT * FROM personas")
resultado = cursor.fetchall()

for persona in resultado:
    print(persona)

# Cerramos la conexion
cursor.close()
conexion.close() # type: ignore
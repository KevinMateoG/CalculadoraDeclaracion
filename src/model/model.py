import sys
import os
sys.path.append("src")
import psycopg2

def ObtenerCursor():
    # Leer configuración de la base de datos desde variables de entorno
    DATABASE = os.getenv('PGDATABASE', 'tu_basedatos')
    USER = os.getenv('PGUSER', 'tu_usuario')
    PASSWORD = os.getenv('PGPASSWORD', 'tu_contraseña')
    HOST = os.getenv('PGHOST', 'localhost')
    PORT = os.getenv('PGPORT', '5432')
    connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    return connection

def ejecutar_script_sql(ruta_script):
    connection = None
    try:
        connection = ObtenerCursor()
        cursor = connection.cursor()
        with open(ruta_script, 'r', encoding='utf-8') as file:
            sql_script = file.read()
        cursor.execute(sql_script)
        connection.commit()
        cursor.close()
        return "Script ejecutado correctamente."
    except Exception as e:
        if connection:
            connection.rollback()
        return f"Error al ejecutar el script: {str(e)}"
    finally:
        if connection:
            connection.close()

def crear_tabla_declaraciones():
    return ejecutar_script_sql('sql/crear_declaraciones.sql')

def crear_tabla_usuarios():
    return ejecutar_script_sql('sql/crear_usuario.sql')

def CrearTabla():
    pass

def BorrarFilas():
    pass

def Insertar():
    pass

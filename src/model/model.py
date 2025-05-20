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

def insertar_declaracion(data):
    connection = None
    try:
        connection = ObtenerCursor()
        cursor = connection.cursor()
        query = """
        INSERT INTO declaraciones (id_declaracion, valor_uvt, ingresos_brutos, costos_deducciones, rentas_exentas, descuentos_tributarios, retenciones_fuente, patrimonio_neto)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            data['id_declaracion'], data['valor_uvt'], data['ingresos_brutos'], data['costos_deducciones'],
            data['rentas_exentas'], data['descuentos_tributarios'], data['retenciones_fuente'], data['patrimonio_neto']
        ))
        connection.commit()
        cursor.close()
        return "Declaración insertada correctamente."
    except Exception as e:
        if connection:
            connection.rollback()
        return f"Error al insertar declaración: {str(e)}"
    finally:
        if connection:
            connection.close()

def modificar_declaracion(id_declaracion, data):
    connection = None
    try:
        connection = ObtenerCursor()
        cursor = connection.cursor()
        query = """
        UPDATE declaraciones
        SET valor_uvt=%s, ingresos_brutos=%s, costos_deducciones=%s, rentas_exentas=%s, descuentos_tributarios=%s, retenciones_fuente=%s, patrimonio_neto=%s
        WHERE id_declaracion=%s
        """
        cursor.execute(query, (
            data['valor_uvt'], data['ingresos_brutos'], data['costos_deducciones'], data['rentas_exentas'],
            data['descuentos_tributarios'], data['retenciones_fuente'], data['patrimonio_neto'], id_declaracion
        ))
        connection.commit()
        cursor.close()
        return "Declaración modificada correctamente."
    except Exception as e:
        if connection:
            connection.rollback()
        return f"Error al modificar declaración: {str(e)}"
    finally:
        if connection:
            connection.close()

def buscar_declaracion(id_declaracion):
    connection = None
    try:
        connection = ObtenerCursor()
        cursor = connection.cursor()
        query = "SELECT * FROM declaraciones WHERE id_declaracion=%s"
        cursor.execute(query, (id_declaracion,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            keys = ['id_declaracion', 'valor_uvt', 'ingresos_brutos', 'costos_deducciones', 'rentas_exentas', 'descuentos_tributarios', 'retenciones_fuente', 'patrimonio_neto']
            return dict(zip(keys, result))
        else:
            return None
    except Exception as e:
        return f"Error al buscar declaración: {str(e)}"
    finally:
        if connection:
            connection.close()

def insertar_usuario(data):
    connection = None
    try:
        connection = ObtenerCursor()
        cursor = connection.cursor()
        query = """
        INSERT INTO users (id_usuario, nombres, apellidos, documento_identidad, fecha_nacimiento, correo)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            data['id_usuario'], data['nombres'], data['apellidos'], data['documento_identidad'], data['fecha_nacimiento'], data['correo']
        ))
        connection.commit()
        cursor.close()
        return "Usuario insertado correctamente."
    except Exception as e:
        if connection:
            connection.rollback()
        return f"Error al insertar usuario: {str(e)}"
    finally:
        if connection:
            connection.close()

def modificar_usuario(id_usuario, data):
    connection = None
    try:
        connection = ObtenerCursor()
        cursor = connection.cursor()
        query = """
        UPDATE users
        SET nombres=%s, apellidos=%s, documento_identidad=%s, fecha_nacimiento=%s, correo=%s
        WHERE id_usuario=%s
        """
        cursor.execute(query, (
            data['nombres'], data['apellidos'], data['documento_identidad'], data['fecha_nacimiento'], data['correo'], id_usuario
        ))
        connection.commit()
        cursor.close()
        return "Usuario modificado correctamente."
    except Exception as e:
        if connection:
            connection.rollback()
        return f"Error al modificar usuario: {str(e)}"
    finally:
        if connection:
            connection.close()

def buscar_usuario(id_usuario):
    connection = None
    try:
        connection = ObtenerCursor()
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id_usuario=%s"
        cursor.execute(query, (id_usuario,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            keys = ['id_usuario', 'nombres', 'apellidos', 'documento_identidad', 'fecha_nacimiento', 'correo']
            return dict(zip(keys, result))
        else:
            return None
    except Exception as e:
        return f"Error al buscar usuario: {str(e)}"
    finally:
        if connection:
            connection.close()

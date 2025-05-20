import sys
sys.path.append(".")
sys.path.append( "src" )

import psycopg2

from model.usuario import Usuario
import SecretConfig

class ControladorUsuarios:

    def CrearTabla():

        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute("""CREATE TABLE if not exists users(id_usuario INT PRIMARY KEY,
                                                           nombres VARCHAR(30),
                                                           apellidos VARCHAR(30),
                                                           documento_identidad VARCHAR(15),
                                                           fecha_nacimiento DATE(11),
                                                           correo VARCHAR(100)
                                                            );
                                                                                    """)
        cursor.connection.commit()

    def EliminarTabla():

        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute("""drop table users""")
        cursor.connection.commit()


    def InsertarUsuario(usuario: Usuario):

        cursor = ControladorUsuarios.ObtenerCursor()
        cursor.execute(f"""insert into users (id_usuario, nombres, apellidos, documento_identidad, fecha_nacimiento, correo) 
                        values ('{usuario.id}', '{usuario.nombres}', '{usuario.apellidos}',  
                                '{usuario.documento_identidad}', '{usuario.fecha_nacimiento}',
                                '{usuario.correo}')""")

        cursor.connection.commit()

    def BuscarUsuario(nombres) -> Usuario:

        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute(f"""select id_usuario, nombres, apellidos, documento_identidad, fecha_nacimiento, correo from usuarios where nombres = '{nombres}'""" )
        fila = cursor.fetchone()
        resultado = Usuario(id=fila[0], nombres=fila[1], apellidos=fila[2], documento_identidad=fila[3], fecha_nacimiento=fila[4], correo=fila[5])
        return resultado
    
    def BuscarPorID(id):
        cursor = ControladorUsuarios.ObtenerCursor()

        consulta = f"""select id_usuario, nombres, apellidos, documento_identidad, fecha_nacimiento, correo from usuarios where id_usuario = '{id}'"""

        cursor.execute(consulta)
        lista = cursor.fetchall()
        if lista is None or lista.__len__ == 0:
            return

        resultado = []

        for fila in lista:                
            usuario = Usuario(id=fila[0], nombres=fila[1], apellidos=fila[2], documento_identidad=fila[3], fecha_nacimiento=fila[4], correo=fila[5])
            resultado.append(usuario)
            
        return resultado

    def ObtenerCursor():
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        cursor = connection.cursor()
        return cursor
    
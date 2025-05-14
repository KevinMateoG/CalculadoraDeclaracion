import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2

from model.Logic_taxes import tax_payment
import SecretConfig

class ControllerDeclarations:
    
    def CrearTabla():
        cursor = ControllerDeclarations.ObtenerCursor()

        with open("sql/crear_declaraciones.sql", "r") as archivo:
            consulta = archivo.read()

        cursor.execute(consulta)
        cursor.connection.commit()

    def BorrarTabla():
        cursor = ControllerDeclarations.ObtenerCursor()

        with open("sql/borrar_declaraciones.sql", "r") as archivo:
            consulta = archivo.read()

        cursor.execute(consulta)
        cursor.connection.commit()

    def Insertar(tax_payment : tax_payment):
        cursor = ControllerDeclarations.ObtenerCursor()
        cursor.execute(f"""INSERT INTO declaraciones (valor_uvt, ingresos_brutos, costos_deducciones, rentas_exentas, descuentos_tributarios, retenciones_fuente, patrimonio_neto)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                       (
                            tax_payment.uvt_value,
                            tax_payment.gross_income,
                            tax_payment.costs_deductions,
                            tax_payment.exempt_income,
                            tax_payment.tax_discounts,
                            tax_payment.withholdings,
                            tax_payment.patrimony

                       )
                       
                       )
        
        cursor.connection.commit()

    def BuscarDeclaracion(id_declaracion) -> tax_payment:
        cursor = ControllerDeclarations.ObtenerCursor()

        cursor.execute(f"""SELECT id_declaracion, valor_uvt, ingresos_brutos, costos_deducciones, rentas_exentas, descuentos_tributarios, retenciones_fuente, patrimonio_neto
                       FROM declaraciones WHERE id_declaracion = '{id}'""")
        fila = cursor.fetchone()
        resultado = tax_payment(uvt_value=fila[0], gross_income=fila[1], costs_deductions=fila[2], exempt_income=fila[3], tax_discounts=fila[4], withholdings=fila[5], patrimony=fila[6])
        return resultado
    
    def ObtenerCursor():
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        cursor = connection.cursor()
        return cursor

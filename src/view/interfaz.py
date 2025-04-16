from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import sys
sys.path.append("src")

from model.Logic_taxes import tax_payment, ErrorRentaExenta, ErrorBaseGravable

class TaxesApp(App):
    def build(self):
        contenedor = GridLayout(cols=2, padding=20, spacing=20)

        contenedor.add_widget(Label(text=" Ingresa el valor de la UVT: "))
        self.tax_base_uvt = TextInput(font_size=30)
        contenedor.add_widget(self.tax_base_uvt)

        contenedor.add_widget(Label(text="Ingrese el ingreso bruto: "))
        self.gross_income = TextInput(font_size=30)
        contenedor.add_widget(self.gross_income)

        contenedor.add_widget(Label(text="Ingrese costos y deducciones: "))
        self.costos_deducciones = TextInput(font_size=30)
        contenedor.add_widget(self.costos_deducciones)

        contenedor.add_widget(Label(text="Ingrese la renta exenta: "))
        self.renta_exenta = TextInput(font_size=30)
        contenedor.add_widget(self.renta_exenta)

        contenedor.add_widget(Label(text="Ingrese los descuentos tributarios: "))
        self.descuentos_tributarios = TextInput(font_size=30)
        contenedor.add_widget(self.descuentos_tributarios)

        contenedor.add_widget(Label(text="Ingrese las retenciones: "))
        self.retenciones = TextInput(font_size=30)
        contenedor.add_widget(self.retenciones)

        contenedor.add_widget(Label(text="Ingrese el patrimonio: "))
        self.patrimonio = TextInput(font_size=30)
        contenedor.add_widget(self.patrimonio)

        self.resultado = Label()
        contenedor.add_widget(self.resultado)

        calcular = Button(text="Calcular", font_size=40)
        contenedor.add_widget(calcular)

        # Conectar con el callback con el evento press del boton
        calcular.bind(on_press=self.saldo_a_favor)

        return contenedor

    def saldo_a_favor(self, value):
        try:
            self.validar()  # Llamar al método de validación
            
            # Obtener los valores de entrada
            uvt_value = float(self.tax_base_uvt.text)
            gross_income = float(self.gross_income.text)
            costs_deductions = float(self.costos_deducciones.text)
            exempt_income = float(self.renta_exenta.text)
            tax_discounts = float(self.descuentos_tributarios.text)
            withholdings = float(self.retenciones.text)
            patrimony = float(self.patrimonio.text)  # Aunque no se usa en el cálculo

            # Llamar a la función de cálculo
            tax_base, tax_base_uvt, rate, calculated_tax, balance_favor = tax_payment(
                uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony
            )

            # Mostrar el resultado
            self.resultado.text = f"Base Gravable: {tax_base}, Base Gravable UVT: {tax_base_uvt}, Tasa: {rate}%, Impuesto Calculado: {calculated_tax}, Saldo a Favor: {balance_favor}"

        except ValueError as err:
            self.resultado.text = "El valor ingresado no es un número válido. Ingrese un número correcto, por ejemplo 500000.00"
        except (ErrorRentaExenta, ErrorBaseGravable) as err:
            self.resultado.text = str(err)
        except Exception as err:
            self.mostrar_error(err)

    def mostrar_error(self, err):
        """ 
        Abre una ventana emergente, con un texto y un botón para cerrar 
        Parámetros: 
        err: Mensaje de error que queremos mostrar en la ventana        
        """

        # contenido es el contenedor donde vamos a agregar los widgets de la ventana
        contenido = GridLayout(cols=1)
        # Creamos el Label que contiene el mensaje de error
        contenido.add_widget(Label(text=str(err)))
        # Creamos el botón para cerrar la ventana
        cerrar = Button(text="Cerrar")
        contenido.add_widget(cerrar)
        # Creamos la ventana emergente con el widget Popup de Kivy
        popup = Popup(title="Error", content=contenido)
        # Conectamos el evento del botón con el método dismiss que cierra el popup
        cerrar.bind(on_press=popup.dismiss)
        # Mostramos la ventana emergente
        popup.open()

    def validar(self):
        """
        Verifica que todos los datos ingresados por el usuario sean correctos
        """
        if not self.tax_base_uvt.text.isnumeric():
            raise ErrorDatosIngresados("El Valor del uvt debe ser un número válido")

        if not self.gross_income.text.isnumeric():
            raise ErrorDatosIngresados("El Número de ingresos brutos debe ser un número válido")

        if not self.costos_deducciones.text.isnumeric():
            raise ErrorDatosIngresados("El valor ingresado de costos y deducciones debe ser un número válido")

        if not self.renta_exenta.text.isnumeric():
            raise ErrorDatosIngresados("El valor ingresado de renta exenta debe ser un número válido")

        if not self.descuentos_tributarios.text.isnumeric():
            raise ErrorDatosIngresados("El valor ingresado de descuentos tributarios debe ser un número válido")

        if not self.retenciones.text.isnumeric():
            raise ErrorDatosIngresados("El valor ingresado de retención en la fuente debe ser un número válido")

        if not self.patrimonio.text.isnumeric():
            raise ErrorDatosIngresados("El valor ingresado de patrimonio debe ser un número válido")

class ErrorDatosIngresados(Exception):
    pass

if __name__ == "__main__":
    TaxesApp().run()

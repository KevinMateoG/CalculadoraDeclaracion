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

class ErrorDatosIngresados(Exception):
    pass

class TaxesApp(App):
    def build(self):
        # Se arma la estructura visual del formulario usando un grid de 2 columnas
        contenedor = GridLayout(cols=2, padding=20, spacing=20)

        # Cada par de líneas crea una etiqueta y un campo de texto para cada dato necesario
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

        # Etiqueta donde se mostrará el resultado final del cálculo
        self.resultado = Label()
        contenedor.add_widget(self.resultado)

        # Botón para realizar el cálculo del impuesto
        calcular = Button(text="Calcular", font_size=40)
        contenedor.add_widget(calcular)

        # Se conecta el botón al método que realizará los cálculos cuando se presione
        calcular.bind(on_press=self.saldo_a_favor)

        return contenedor

    def saldo_a_favor(self, value):
        try:
            self.validar() 
            # Recuperación de todos los datos ingresados por el usuario
            uvt_value = float(self.tax_base_uvt.text)
            gross_income = float(self.gross_income.text)
            costs_deductions = float(self.costos_deducciones.text)
            exempt_income = float(self.renta_exenta.text)
            tax_discounts = float(self.descuentos_tributarios.text)
            withholdings = float(self.retenciones.text)
            patrimony = float(self.patrimonio.text) 

            # Se llama la función lógica que contiene el cálculo del impuesto
            tax_base, tax_base_uvt, rate, calculated_tax, balance_favor = tax_payment(
                uvt_value, gross_income, costs_deductions, exempt_income, tax_discounts, withholdings, patrimony
            )

            # Se prepara el resumen del resultado para mostrarlo en pantalla
            self.resultado.text = f"Base Gravable: {tax_base}, Base Gravable UVT: {tax_base_uvt}, Tasa: {rate}%, Impuesto Calculado: {calculated_tax}, Saldo a Favor: {balance_favor}"

        # Si se ingresa texto no numérico, se lanza este mensaje
        except ValueError as err:
            self.resultado.text = "El valor ingresado no es un número válido. Ingrese un número correcto, por ejemplo 500000.00"

        # Captura errores específicos del modelo de cálculo
        except (ErrorRentaExenta, ErrorBaseGravable) as err:
            self.resultado.text = str(err)

        # Por si ocurre un error, se lanza una ventana con detalles del error.
        except Exception as err:
            self.mostrar_error(err)

    def mostrar_error(self, err):
        """ 
        Crea una ventana emergente sencilla para mostrar errores que no estaban previstos 
        """

        # Este layout contiene el mensaje y el botón de cierre
        contenido = GridLayout(cols=1)
        contenido.add_widget(Label(text=str(err)))
        cerrar = Button(text="Cerrar")
        contenido.add_widget(cerrar)

        popup = Popup(title="Error", content=contenido)

        # Acción que permite cerrar la ventana al presionar el botón
        cerrar.bind(on_press=popup.dismiss)
        popup.open()

    def validar(self):
        """
        Pequeña revisión para evitar errores comunes al digitar los datos
        """
        # A continuación se revisa campo por campo si lo ingresado es un valor ingresado vállido. 
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


if __name__ == "__main__":
    TaxesApp().run()

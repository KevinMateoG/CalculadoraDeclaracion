from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import sys
sys.path.append("src")

from model.Logic_taxes import tax_payment

class TaxesApp (App):
    def build(self):
        contenedor = GridLayout(cols=2,padding=20,spacing=20)

        contenedor.add_widget( Label(text=" Ingresa el valor de la UVT: ") )
        self.tax_base_uvt = TextInput(font_size=30 )
        contenedor.add_widget(self.tax_base_uvt)

        contenedor.add_widget( Label(text="Ingrese el ingreso bruto: ") )
        self.tax_base = TextInput(font_size=30 )
        contenedor.add_widget(self.tax_base)

        contenedor.add_widget( Label(text="Ingrese costos y deducciones: ") )
        self.tax_base = TextInput(font_size=30 )
        contenedor.add_widget(self.tax_base)

        contenedor.add_widget( Label(text="Ingrese la renta exenta: ") )
        self.tax_base = TextInput(font_size=30 )
        contenedor.add_widget(self.tax_base)

        contenedor.add_widget( Label(text="Ingrese los descuentos tributarios: ") )
        self.calculated_tax = TextInput(font_size=30 )
        contenedor.add_widget(self.calculated_tax)

        contenedor.add_widget( Label(text="Ingrese las retenciones: ") )
        self.calculated_tax = TextInput(font_size=30 )
        contenedor.add_widget(self.calculated_tax)

        contenedor.add_widget( Label(text="Ingrese el patrimonio: ") )
        self.calculated_tax = TextInput(font_size=30 )
        contenedor.add_widget(self.calculated_tax)

        self.resultado = Label()
        contenedor.add_widget(self.resultado)

        calcular = Button(text="Calcular",font_size=40)
        contenedor.add_widget(calcular)

        # Conectar con el callback con el evento press del boton
        calcular.bind( on_press=self.saldo_a_favor )

        return contenedor
    
    # instance es el widget que generó el evento
    # value es el valor actual que tiene el widget
    def saldo_a_favor( self, value ):
        try:
            self.validar()
            saldo = tax_payment( amount=float(self.calculated_tax.text))
            self.resultado.text = str( round( saldo, 2)  )

        except ValueError as err:
            self.resultado.text = "El valor ingresado no es un numero válido. Ingrese un numero correcto, por ejemplo 500000.00"
        except Exception as err:
            self.mostrar_error( err )
        
    def mostrar_error( self, err ):
        """ 
        Abre una ventana emergente, con un texto y un botón para cerrar 
        Parámetros: 
        err: Mensaje de error que queremos mostrar en la ventana        
        """

        # contenido es el contenedor donde vamos a agregar los widgets de la ventana
        contenido = GridLayout(cols=1)
        # Creamos el Label que contiene el mensaje de error
        contenido.add_widget( Label(text= str(err) ) )
        # Creamos el botón para cerrar la ventana
        cerrar = Button(text="Cerrar" )
        contenido.add_widget( cerrar )
        # Creamos la ventana emergente con el widget Popup de Kivy
        popup = Popup(title="Error",content=contenido)
        # Conectamos el evento del botón con el método dismiss que cierra el popup
        cerrar.bind( on_press=popup.dismiss)
        # Mostramos la ventana emergente
        popup.open()

class ErrorDatosIngresados(Exception):
    pass

    def validar(self):
        """
        Verifica que todos datos ingresados por el usuario sean correctos
        """
        if( not( self.tax_base_uvt.text.isnumeric() )  ):
            raise ErrorDatosIngresados( "El Valor del uvt debe ser un número válido"  )
        
        if( not( self.tax_base.text.isnumeric() )  ):
            raise ErrorDatosIngresados( "El Número de ingresos brutos debe ser un número válido"  )

        if( not( self.calculated_tax.text.isnumeric() )  ):
            raise ErrorDatosIngresados( "El valor ingresado de costos y deducciones debe ser un número válido"  )
        
        if( not( self.calculated_tax.text.isnumeric() )  ):
            raise ErrorDatosIngresados( "El valor ingresado de renta exenta debe ser un número válido"  )

        if( not( self.calculated_tax.text.isnumeric() )  ):
            raise ErrorDatosIngresados( "El valor ingresado de descuentos tributarios debe ser un número válido"  )

        if( not( self.calculated_tax.text.isnumeric() )  ):
            raise ErrorDatosIngresados( "El valor ingresado de retención en la fuente debe ser un número válido"  )

        if( not( self.calculated_tax.text.isnumeric() )  ):
            raise ErrorDatosIngresados( "El valor ingresado de patrimonio debe ser un número válido"  )
        
if __name__ == "__main__":
    TaxesApp().run()

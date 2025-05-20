from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

import sys
sys.path.append("src")
from model import model

class SqlInterfaceApp(App):
    def build(self):
        self.layout = GridLayout(cols=2, padding=20, spacing=10)

        # Status label
        self.status_label = Label(text="Seleccione una acción")
        self.layout.add_widget(self.status_label)
        self.layout.add_widget(Label())  # empty cell

        # --- Declaraciones inputs ---
        self.layout.add_widget(Label(text="ID Declaración:"))
        self.id_declaracion = TextInput(multiline=False)
        self.layout.add_widget(self.id_declaracion)

        self.layout.add_widget(Label(text="Valor UVT:"))
        self.valor_uvt = TextInput(multiline=False)
        self.layout.add_widget(self.valor_uvt)

        self.layout.add_widget(Label(text="Ingresos Brutos:"))
        self.ingresos_brutos = TextInput(multiline=False)
        self.layout.add_widget(self.ingresos_brutos)

        self.layout.add_widget(Label(text="Costos y Deducciones:"))
        self.costos_deducciones = TextInput(multiline=False)
        self.layout.add_widget(self.costos_deducciones)

        self.layout.add_widget(Label(text="Rentas Exentas:"))
        self.rentas_exentas = TextInput(multiline=False)
        self.layout.add_widget(self.rentas_exentas)

        self.layout.add_widget(Label(text="Descuentos Tributarios:"))
        self.descuentos_tributarios = TextInput(multiline=False)
        self.layout.add_widget(self.descuentos_tributarios)

        self.layout.add_widget(Label(text="Retenciones Fuente:"))
        self.retenciones_fuente = TextInput(multiline=False)
        self.layout.add_widget(self.retenciones_fuente)

        self.layout.add_widget(Label(text="Patrimonio Neto:"))
        self.patrimonio_neto = TextInput(multiline=False)
        self.layout.add_widget(self.patrimonio_neto)

        # Buttons for declaraciones
        btn_insertar_decl = Button(text="Insertar Declaración")
        btn_insertar_decl.bind(on_press=self.insertar_declaracion)
        self.layout.add_widget(btn_insertar_decl)

        btn_modificar_decl = Button(text="Modificar Declaración")
        btn_modificar_decl.bind(on_press=self.modificar_declaracion)
        self.layout.add_widget(btn_modificar_decl)

        btn_buscar_decl = Button(text="Buscar Declaración")
        btn_buscar_decl.bind(on_press=self.buscar_declaracion)
        self.layout.add_widget(btn_buscar_decl)

        self.layout.add_widget(Label())  # empty cell

        # --- Usuarios inputs ---
        self.layout.add_widget(Label(text="ID Usuario:"))
        self.id_usuario = TextInput(multiline=False)
        self.layout.add_widget(self.id_usuario)

        self.layout.add_widget(Label(text="Nombres:"))
        self.nombres = TextInput(multiline=False)
        self.layout.add_widget(self.nombres)

        self.layout.add_widget(Label(text="Apellidos:"))
        self.apellidos = TextInput(multiline=False)
        self.layout.add_widget(self.apellidos)

        self.layout.add_widget(Label(text="Documento Identidad:"))
        self.documento_identidad = TextInput(multiline=False)
        self.layout.add_widget(self.documento_identidad)

        self.layout.add_widget(Label(text="Fecha Nacimiento (YYYY-MM-DD):"))
        self.fecha_nacimiento = TextInput(multiline=False)
        self.layout.add_widget(self.fecha_nacimiento)

        self.layout.add_widget(Label(text="Correo:"))
        self.correo = TextInput(multiline=False)
        self.layout.add_widget(self.correo)

        # Buttons for usuarios
        btn_insertar_user = Button(text="Insertar Usuario")
        btn_insertar_user.bind(on_press=self.insertar_usuario)
        self.layout.add_widget(btn_insertar_user)

        btn_modificar_user = Button(text="Modificar Usuario")
        btn_modificar_user.bind(on_press=self.modificar_usuario)
        self.layout.add_widget(btn_modificar_user)

        btn_buscar_user = Button(text="Buscar Usuario")
        btn_buscar_user.bind(on_press=self.buscar_usuario)
        self.layout.add_widget(btn_buscar_user)

        return self.layout

    def mostrar_popup(self, titulo, mensaje):
        contenido = GridLayout(cols=1, padding=10)
        contenido.add_widget(Label(text=mensaje))
        btn_cerrar = Button(text="Cerrar", size_hint_y=None, height=40)
        contenido.add_widget(btn_cerrar)

        popup = Popup(title=titulo, content=contenido, size_hint=(0.7, 0.4))
        btn_cerrar.bind(on_press=popup.dismiss)
        popup.open()

    def obtener_datos_declaracion(self):
        try:
            data = {
                'id_declaracion': int(self.id_declaracion.text),
                'valor_uvt': float(self.valor_uvt.text),
                'ingresos_brutos': float(self.ingresos_brutos.text),
                'costos_deducciones': float(self.costos_deducciones.text),
                'rentas_exentas': float(self.rentas_exentas.text),
                'descuentos_tributarios': float(self.descuentos_tributarios.text),
                'retenciones_fuente': float(self.retenciones_fuente.text),
                'patrimonio_neto': float(self.patrimonio_neto.text)
            }
            return data
        except ValueError:
            self.mostrar_popup("Error", "Por favor ingrese valores numéricos válidos para la declaración.")
            return None

    def obtener_datos_usuario(self):
        data = {
            'id_usuario': int(self.id_usuario.text) if self.id_usuario.text.isdigit() else None,
            'nombres': self.nombres.text,
            'apellidos': self.apellidos.text,
            'documento_identidad': self.documento_identidad.text,
            'fecha_nacimiento': self.fecha_nacimiento.text,
            'correo': self.correo.text
        }
        if data['id_usuario'] is None:
            self.mostrar_popup("Error", "El ID de usuario debe ser un número válido.")
            return None
        return data

    def insertar_declaracion(self, instance):
        data = self.obtener_datos_declaracion()
        if data:
            resultado = model.insertar_declaracion(data)
            self.mostrar_popup("Insertar Declaración", resultado)

    def modificar_declaracion(self, instance):
        data = self.obtener_datos_declaracion()
        if data:
            resultado = model.modificar_declaracion(data['id_declaracion'], data)
            self.mostrar_popup("Modificar Declaración", resultado)

    def buscar_declaracion(self, instance):
        try:
            id_declaracion = int(self.id_declaracion.text)
        except ValueError:
            self.mostrar_popup("Error", "Ingrese un ID de declaración válido para buscar.")
            return
        resultado = model.buscar_declaracion(id_declaracion)
        if isinstance(resultado, dict):
            self.id_declaracion.text = str(resultado['id_declaracion'])
            self.valor_uvt.text = str(resultado['valor_uvt'])
            self.ingresos_brutos.text = str(resultado['ingresos_brutos'])
            self.costos_deducciones.text = str(resultado['costos_deducciones'])
            self.rentas_exentas.text = str(resultado['rentas_exentas'])
            self.descuentos_tributarios.text = str(resultado['descuentos_tributarios'])
            self.retenciones_fuente.text = str(resultado['retenciones_fuente'])
            self.patrimonio_neto.text = str(resultado['patrimonio_neto'])
            self.mostrar_popup("Buscar Declaración", "Declaración encontrada y cargada en el formulario.")
        else:
            self.mostrar_popup("Buscar Declaración", resultado or "Declaración no encontrada.")

    def insertar_usuario(self, instance):
        data = self.obtener_datos_usuario()
        if data:
            resultado = model.insertar_usuario(data)
            self.mostrar_popup("Insertar Usuario", resultado)

    def modificar_usuario(self, instance):
        data = self.obtener_datos_usuario()
        if data:
            resultado = model.modificar_usuario(data['id_usuario'], data)
            self.mostrar_popup("Modificar Usuario", resultado)

    def buscar_usuario(self, instance):
        try:
            id_usuario = int(self.id_usuario.text)
        except ValueError:
            self.mostrar_popup("Error", "Ingrese un ID de usuario válido para buscar.")
            return
        resultado = model.buscar_usuario(id_usuario)
        if isinstance(resultado, dict):
            self.id_usuario.text = str(resultado['id_usuario'])
            self.nombres.text = resultado['nombres']
            self.apellidos.text = resultado['apellidos']
            self.documento_identidad.text = resultado['documento_identidad']
            self.fecha_nacimiento.text = resultado['fecha_nacimiento']
            self.correo.text = resultado['correo']
            self.mostrar_popup("Buscar Usuario", "Usuario encontrado y cargado en el formulario.")
        else:
            self.mostrar_popup("Buscar Usuario", resultado or "Usuario no encontrado.")

if __name__ == "__main__":
    SqlInterfaceApp().run()

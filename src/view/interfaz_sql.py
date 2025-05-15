from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

import sys
sys.path.append("src")
from model import model

class SqlInterfaceApp(App):
    def build(self):
        self.layout = GridLayout(cols=1, padding=20, spacing=20)

        self.status_label = Label(text="Seleccione una acción para crear tablas")
        self.layout.add_widget(self.status_label)

        btn_crear_declaraciones = Button(text="Crear tabla declaraciones")
        btn_crear_declaraciones.bind(on_press=self.crear_declaraciones)
        self.layout.add_widget(btn_crear_declaraciones)

        btn_crear_usuarios = Button(text="Crear tabla usuarios")
        btn_crear_usuarios.bind(on_press=self.crear_usuarios)
        self.layout.add_widget(btn_crear_usuarios)

        return self.layout

    def mostrar_popup(self, titulo, mensaje):
        contenido = GridLayout(cols=1, padding=10)
        contenido.add_widget(Label(text=mensaje))
        btn_cerrar = Button(text="Cerrar", size_hint_y=None, height=40)
        contenido.add_widget(btn_cerrar)

        popup = Popup(title=titulo, content=contenido, size_hint=(0.7, 0.4))
        btn_cerrar.bind(on_press=popup.dismiss)
        popup.open()

    def crear_declaraciones(self, instance):
        resultado = model.crear_tabla_declaraciones()
        self.mostrar_popup("Resultado", resultado)

    def crear_usuarios(self, instance):
        resultado = model.crear_tabla_usuarios()
        self.mostrar_popup("Resultado", resultado)

if __name__ == "__main__":
    SqlInterfaceApp().run()

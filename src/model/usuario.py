from datetime import date

class Usuario:
    def __init__(self, id, nombres, apellidos, documento_identidad, fecha_nacimiento, correo):

        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.documento_identidad = documento_identidad
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo

    def esIgual(self, comparar_con) :
        
        assert(self.id == comparar_con.id)
        assert(self.nombres == comparar_con.nombres)
        assert(self.apellidos == comparar_con.apellidos)
        assert(self.documento_identidad == comparar_con.documento_identidad)
        assert(self.fecha_nacimiento == comparar_con.fecha_nacimiento)
        assert(self.correo == comparar_con.correo)   

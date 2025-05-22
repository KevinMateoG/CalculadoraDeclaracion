from flask import Flask, render_template, request, Blueprint

blueprint = Blueprint("vista", __name__, "templates")

import sys
sys.path.append("src")

from controller.controller_users import ControladorUsuarios
import SecretConfig

@blueprint.route("/vista")
def vista():
    return render_template("index.html")

@blueprint.route('/')      
def index():
    return render_template("index.html")

@blueprint.route('/buscar')
def buscar():
    return render_template('buscar.html')

@blueprint.errorhandler(Exception)
def controlar_errores(err):
    return "ocurrio un error con los datos ingresados :" + str(err)

@blueprint.route('/lista_tarjetas')
def lista_tarjetas():
    usuario = ControladorUsuarios.BuscarPorID( request.args["id_usuario"]  )
    return render_template('lista_tarjetas.html', Id_usuario=request.args["id_usuario"], usuario=usuario  )

@blueprint.errorhandler(Exception)
def controlar_errores(err):
    return "Ocurrió un error mi papacho, sucedió lo siguiente: "  +str(err)

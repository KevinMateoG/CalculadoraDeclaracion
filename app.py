from flask import Flask    

from flask import render_template, request

import sys
sys.path.append( "src" )

from controller.controller_users import ControladorUsuarios

app = Flask(__name__)     

@app.route('/')      
def index():
    return render_template("index.html")

@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.errorhandler(ValueError)
def controlar_errores(err):
    return "ocurrio un error con los datos ingresados :" + str(err)

@app.route('/lista_tarjetas')
def lista_tarjetas():
    usuario = ControladorUsuarios.BuscarPorID( request.args["id_usuario"]  )
    return render_template('lista_tarjetas.html', Id_usuario=request.args["id_usuario"], usuario=usuario  )

@app.errorhandler(Exception)
def controlar_errores(err):
    return "Ocurrió un error mi papacho, sucedió lo siguiente: "  +str(err)

if __name__=='__main__':
   app.run( debug=True)

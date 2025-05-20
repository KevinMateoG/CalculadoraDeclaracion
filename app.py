from flask import Flask    

from flask import render_template, request

import sys
sys.path.append( "src" )

from controller.controller_users import * 


app = Flask(__name__)     

@app.route('/')      
def index():
    return render_template("index.html")
  
@app.route('/formulario')  
def hello_html():
    usuarios = ControladorUsuarios.BuscarPorID(request.args["id_usuario"])
    return render_template( 'formulario.html', id_usuario=request.args["id_usuario"], usuarios = usuarios )


if __name__=='__main__':
   app.run( debug=True)
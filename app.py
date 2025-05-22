from flask import Flask    

from flask import render_template, Blueprint

import sys
sys.path.append( "src" )

from controller.controller_users import ControladorUsuarios
from view.web import tales

app = Flask(__name__)     

app.register_blueprint(tales.blueprint)

if __name__=='__main__':
   app.run( debug=True)
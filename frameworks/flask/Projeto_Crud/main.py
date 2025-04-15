from flask import Flask
from routes.cliente import cliente_route 
# pegando a variavel do blueprint 
from routes.home import home_route

app = Flask(__name__)

# registrando blueprint
app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')

app.run(debug=True)
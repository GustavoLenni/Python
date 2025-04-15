# rotas referentes a pagina principal
# blue print agrupa rotas dentro de um agrupador (dentro desse grupo tem varias rotas
# referentes a esse grupo )

from  flask import Blueprint, render_template

# criando blueprint
home_route = Blueprint('home', __name__)

# rota principal
@home_route.route('/')

def home():
    return render_template('index.html')
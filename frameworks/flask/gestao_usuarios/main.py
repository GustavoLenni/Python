# Importando o flask 
# from flask (modulo flask) vai importar a classe Flask com (F)Maiusculo
# url_for é para pegar urls internas do servidor web linkar (redirecionamento de pages)
# render_template serve para buscar na pasta templates um arquivo html quanto para mandar
# variaveis do back-end para o front-end atráves das variaveis de contexto 
from flask import Flask,render_template,url_for

# inicializando o flask
# o (__name__) é para identificar e organizar os recursos do nosso projeto 
app = Flask(__name__)

# rotas
@app.route("/")
def Inicio():
    # retornar informações das variaveis de contexto do back-end para o front-end 
    titulo = "Gestão de Usuarios"
    usuarios = [
        {"nome": "Guilherme", "nembro_ativo":True},
        {"nome": "Gustavo", "nembro_ativo":False}
    ]
    return render_template('index.html',titulo=titulo, usuarios=usuarios)
# chamando o meu html 

@app.route("/sobre")
def pagina_sobre():
    return """
        <b>Programador Python</b>:Assita os videos no
        <a href"https://www.youtube.com/watch?v=fkXlSyWiXVg&t=1s">Canal Do Youtube</a>
"""

# executando servidor web
# o debug=true é uma forma de dizer ao flask que estamos no modo desenvolvedor
app.run(debug=True)
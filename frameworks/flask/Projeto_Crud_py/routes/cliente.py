# rotas para clientes 
from  flask import Blueprint,render_template
from database.cliente import CLIENTES

# criando blueprint
cliente_route = Blueprint('cliente', __name__)

# Prefixo do clientes rota dos clientes 
# - /clientes/ (GET) - listar os clientes 
# - /clientes/ (POST) - Inserir o cliente no servidor 
# - /clientes/new (GET) - rendezirar um forms para criar um cliente 
# - /clientes/<id> (GET) - obter os dados dos clientes 
# - /clientes/<id>/edit (GET) - renderizar um forms para editar um cliente  
# - /clientes/<id>/update (PUT) - Atualizar os dados do cliente 
# - /clientes/<id>/delete (DELETE) - Deletar o registro do usuario


# rota principal
@cliente_route.route('/')
# listar os clientes 
def lista_clientes():
    return render_template('lista_clientes.html', clientes = CLIENTES)

# @cliente_route.route('/',  methods=['POST'])
# # inserir os dados do cliente 
# def inserir_cliente():
#     pass

# @cliente_route.route('/new')
# def form_cliente():
#     # form para cadastrar cliente 
#     return render_template('form_cliente.html')

# @cliente_route.route('/<int:cliente_id>')
# def obter_cliente(cliente_id):
#     # exibir detalhe dos clientes
#     return render_template('detalhe_cliente.html')

# @cliente_route.route('/<int:cliente_id>/edit')
# def form_edit_cliente(cliente_id):
#     # form para editar cliente 
#     return render_template('form_edit_cliente.html')

# @cliente_route.route('/<int:cliente_id>/update', methods= ['PUT'])
# def atualizar_cliente(cliente_id):
#     # Atualizar dados do cliente 
#     pass


# @cliente_route.route('/<int:cliente_id>/delete', methods= ['DELETE'])
# def deletar_cliente(cliente_id):
#     # deletar o registro do usuario 
#     pass



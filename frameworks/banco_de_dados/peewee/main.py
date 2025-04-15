from database import db, Usuario, Anuncio

# conectar banco de dados 
db.connect()

#  criar as tabelas caso elas não existam no banco de dados 
db.create_tables([Usuario,Anuncio])

usuario = Usuario.create(nome="Programador", email="programador@gmail.com",senha="123")
# como criamos no nosso banco de dados que o email é unico se repetirmos o código com o mesmo
#  email vai dar erro 

print("Novo usuario: ", usuario.id,usuario.nome, usuario.email)

# Usuario.create(nome="Gustavo", email="gu@gmail.com",senha="12345")
# Usuario.create(nome="Guilherme", email="gui@gmail.com",senha="1234567")
# Usuario.create(nome="Lenilson", email="lenni@gmail.com",senha="1234590009")

# listando todos os usuarios da tabela 

# lista_usuarios = Usuario.select()
# print("Lista De Usuarios: ")

# for i in lista_usuarios:
#     print("-", i.id,i.nome,i.email)

# filtrando usuario pelo id
# usuario1 = Usuario.get(Usuario.id == 1)
# print("usuario pelo id: ", usuario1.id, usuario1.nome)

# filtrando usuario pelo email
# usuario2 = Usuario.get(Usuario.email == "gui@gmail.com")
# print("Usuario de Email de:",usuario2.id,usuario2.nome, usuario2.email)


# Update filtrando pelo Usuario
# Lenilson = Usuario.get(Usuario.id == 3)
# Lenilson.nome = "Lenilson Python"
# Lenilson.save()

# print("Usuario atualizado:",Lenilson.id, Lenilson.nome)

# Tentando criar usuario com email duplicado 
# try:
#     usuario_duplicado = Usuario.create(nome="Gustavo Python", email="gu@gmail.com",senha="123")
# except:
#     print("Email já existente")


# Deletando Usuarios
# usuario_deletado = Usuario.get(Usuario.email == "gu@gmail.com")
# usuario_deletado.delete_instance()

# try:
#     Usuario.get(Usuario.email == "gu@gmail.com")
# except:
#     print("Usuario Deletado")


# Adionando informações na tabela Anuncio 
# Gui = Usuario.get(Usuario.email == "gui@gmail.com")

# anuncio = Anuncio.create(
#     usuario = Gui,
#     titulo = "Video",
#     descricao = "Video Legal",
#     valor = 500
# ) 
# print("Novo Anuncio", anuncio.id, anuncio.titulo)

# Anuncio.create(usuario = Gui,titulo = "Video",descricao = "Opa", valor = 1000)
# Anuncio.create(usuario = Gui,titulo = "Video1",descricao = "Opa1", valor = 350)
# Anuncio.create(usuario = Gui,titulo = "Video2",descricao = "Opa2", valor = 7000)


# filtrando e vendo anuncios do usuario
# print("Anuncios do Gui:")
# anuncios_gui = Anuncio.select().join(Usuario).where(Usuario.email == "gui@gmail.com")
# for a in anuncios_gui:
#     print("-", a.id,a.titulo,a.valor)


# Vendo e deletando anuncios
# Anuncio.delete().execute()
# print("Quantidade de Anuncios", Anuncio.select().count())


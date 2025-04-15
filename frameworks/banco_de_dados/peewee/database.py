# importando o peewee
from peewee import *

# criando o banco de dados
db = SqliteDatabase('freela.db')

# criando uma tabela no banco de dados 
#  a chave primaria no peewee ja é gerada automaticamente 
class Usuario(Model):
    nome = CharField()
    email = CharField(unique= True)
    senha = CharField()

#  para o peewee entender em qual banco de dados a tabela será criada 
    class Meta:
        database =  db

class Anuncio(Model):
    usuario = ForeignKeyField(Usuario, backref='usuarios')
    # backref nome de referencia 
    titulo = CharField()
    descricao = TextField()
    valor = DecimalField()
    
    class Meta:
        database = db


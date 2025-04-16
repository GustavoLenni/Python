import random 
import string

def gerar_senha(tamanho,usar_maiusculas,usar_numeros,usar_simbolos):
    # começa com os caracters minusculos
    caracters = string.ascii_lowercase
    if usar_maiusculas:
        caracters += string.ascii_uppercase
    if usar_numeros:
        caracters += string.digits
    if usar_simbolos:
        caracters += string.punctuation

    senha = ''.join(random.choice(caracters) for _ in range(tamanho))
    return senha

tamanho = int(input("Digite o Tamanho da Senha: "))
# esses input e ifs basicamente fazem isso 

# Pegando o input
# Transformando ele num valor booleano (True ou False)
# Usando esse valor pra controlar o if depois
# ele contrala esse if pelo lower pq o if ja é boolean ou seja true e false 


usar_maiusculas = input("Incluir Letras Maiusculas? (s/n)").lower() =='s'
usar_numeros = input("Incluir Números? (s/n)").lower() =='s'
usar_simbolos = input("Incluir simbolos? (s/n)").lower() == 's'
# esse .lower == 's' faz com que se o usuario colocar s tanto maisculo como minusculo ele reconheça
# que é para usar o if caso for outra letra sem ser o s ele retorna false 


senha = gerar_senha(tamanho,usar_maiusculas,usar_numeros,usar_simbolos)
print(f"Senha Gerada: {senha}",)
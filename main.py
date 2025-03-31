# Exibir informações
# print("Quero meu primeiro emprego");
# print é uma forma de exibir informações no terminal 


# Variaveis
# nome = "Gustavo";
# idade = 18;
# peso = 65.5;

# print(nome)
# print(idade)
# print(peso)


# Boolean 
# is_python = true;
# is_java = false;

# ingresso = 50;
# compradores = 250;
# tem_ingresso_suficiente = (ingresso >= compradores);
# print(tem_ingresso_suficiente);


# Inputs (entrada do usuario)
# nome = input("Digite seu nome: ");
# idade = int(input("Digite sua idade: "));
# peso = float(input("Digite seu peso: "));

# print(nome);
# print(idade);
# print(peso);


# Operadores
# soma = 1+1;
# multiplicacao = 4 * 4;
# divisao = 30/3;
# potencia = 7 ** 2;

# print("Soma: ", soma)
# print("Multiplicação: ", multiplicacao)
# print("divisao: ", divisao)
# print("Potencia: ", potencia)

# Condicionais
# idade = int(input("Digite sua idade: "));

# if idade >=  18:
#     print("Permitido")
# else:
#     print("Não é permitido")

# condição e adicional (and)
# salario = float(input("Digite seu Salario: "));

# if salario <= 3000:
#     print("Programador Junior")
# elif salario >= 3000 and salario <= 6000:
#     print("Programador Pleno")
# elif salario >= 6000 and salario <= 15000:
#     print("Programador Senior")
# else:
#     print("Gerente de projetos")


# listas (Arrays)
# lista_numeros = [1,2,3]

# lista_numeros[0] = 5

# print(lista_numeros[0])
# print(lista_numeros[1])
# print(lista_numeros[2])

# numeros = [1,2,3]
# strings = ["Gustavo", "Lenilson", "Claudia", "Guilherme","Dona Maria"]
# decimais = [10.7, 8.9, 76.7]

# lista_vazia = []

# lista_vazia.append("Olá")
# lista_vazia.append("Mundo")

# print(lista_vazia)


# Repetições (For e While)
# notas = []

# for x in range(5):
#     codigo_aluno = int(input("RM:"))
#     nota = float(input("Nota:"))
#     # no resultado ele define o indice 0 para o codigo aluno e 1 para a nota
#     resultado = [codigo_aluno, nota]
#     # adiciona o resultado na variavel notas 
#     notas.append(resultado)

# print("Quantidade de notas dos alunos", len(notas))

# for n in notas:
#     # pega o valor do indice do codigo aluno e retorna o a informação do usuario 
#     codigo_aluno = n[0]
#     #  mesma coisa para nota pegando o indice 
#     nota = n[1]
#     print("Rm: ", codigo_aluno, "Nota: ", nota)

# notas = []

# contador = 1
# # o contador inicia com 1

# while contador <= 5:
#     # quando o contador for 6 o loop para 
#     codigo_aluno = int(input("RM: "))
#     nota = float(input("Nota: "))
#     resultado = [codigo_aluno, nota]
#     notas.append(resultado)

#     #  ele adiciona mais 1 ao contador para o loop não ser infinito
#     # porque o numero 1 sempre é menor que 5 e nunca iria chegar a 6 para parar o loop
#     # gerando assim um loop infinito 
#     contador = contador+1
#     # ou 
#     #  contador += 1

# print("Quantidade de notas dos alunos: ", len(notas))


# Dicionarios ou Objetos 

# pessoas = {
#     "nome": "Gustavo Lenni",
#     "idade": 18,
#     "peso": 70.5
# }

# print(pessoas['nome'])
# print(pessoas['idade'])
# print(pessoas['peso'])

# player = {
#     "Nome": "Gustavo",
#     "Vida": 200,
#     "Dano": 40,
# }
# npcs = [
#     {"Nome": "NPC-1", "Vida": 50, "Dano":1},    
#     {"Nome": "NPC-2", "Vida": 50, "Dano":1},
#     {"Nome": "NPC-3", "Vida": 50, "Dano":1},
#     {"Nome": "MONSTRO-1", "Vida": 100, "Dano":20},
#     {"Nome": "CHEFE-1", "Vida": 550, "Dano":50},
#     ]


#Chat 
# Importando scripts 
# import os

# mensagens = []

# nome = input("Nome: ")

# while True:

#     os.system('cls')

#     if len(mensagens) > 0:
#         for i in mensagens:
#             print( i ['nome'], "-", i ['texto'])
    
#     print("______________________")

#     texto = input("mensagem: ")
#     if texto == 'fim':
#         break

#     mensagens.append({
#         "nome": nome,
#         "texto": texto
#     })


# Funções 
# print("Realize sua soma")

# def funcao(valor1, valor2):
#     return valor1 + valor2

# contador = 1
# while contador <= 5:
    
#     valor1 = int(input("Valor1: "))
#     valor2 = int(input("Valor2: "))
    
#     resultado = funcao(valor1,valor2)
#     print( valor1, "+",valor2, "=", resultado)
#     print("------------")
#     contador = contador+1

# caixa = []

# print("Fluxo de Caixa")
# print("Opção 1: Adicionar Receita")
# print("Opção 2: Adicionar Despesa")
# print("Digite outro número para finalizar")


# def transacao(opcao):
#     nome = str(input("Nome: "))
#     valor = float(input("Valor: "))
#     caixa.append({ 
#         "nome":nome,
#         "valor":valor,
#     })
#     print("----------------")

# while True:
#     opcao = int(input("Digite a Opção: "))

#     if opcao == 1 or opcao == 2:
#         transacao(opcao)
#     else:
#         break


# total = 0
# for i in caixa:
#     print("-------------")
#     print("Nome: ", i['nome'], "Valor R$: ", i['valor'])
#     total = total + i['valor']
#     print("Saldo Atual R$: ", total)


# Estrutura With

# Sem o with 
# arquivo = open("meu_arquivo.txt" ,"w")
# # Abrindo o arquivo
# # o "w" é de write ou seja para escrever no arquivo
# # ou "r" que seria read para ler o arquivo
# arquivo.write("Hello World")
# # escrevendo "Hello World no Arquivo"
# arquivo.close()
# # Fechando o Arquivo

# com o with
# with open("meu_arquivo.txt", 'w') as arquivo:
#     # O 'open("meu_arquivo.txt", 'w')' abre o arquivo no modo de escrita ('w' de write).
#     # Se o arquivo não existir, ele será criado. Se já existir, o conteúdo será apagado.
    
#     # O 'with' garante que o arquivo será fechado automaticamente ao final do bloco.
    
#     arquivo.write("Olá Mundo")  # Escreve "Olá Mundo" no arquivo.
    
#     # Após sair do bloco 'with', o arquivo será fechado automaticamente.

#Utilizando para ler o arquivo 
# with open("meu_arquivo.txt", 'r') as arquivo:
#     print(arquivo.read())



# Classes e Programação orientada a Objetos

# class Vendedor():
#     def __init__(self, nome):
#         self.nome = nome
    
#     def vendeu(self,vendas):
#         self.vendas = vendas
    
#     def meta(self,meta):
#         if self.vendas >= meta:
#             print(self.nome, "Bateu A meta Com o total de:", self.vendas, "Vendas")
#         else:
#             print(self.nome, "Não Bateu a meta de: ", meta, "Vendas")

# vendedores = []
# for x in range(2):
#     vendedor1 = Vendedor(input("Nome: "))
#     vendedor1.vendeu(int(input("Vendas: ")))
#     vendedor1.meta(int(input("Meta: ")))
#     vendedores.append(vendedor1)

# print("Tivemos o total de: ", len(vendedores), "Vendedores")


class ControleRemoto:
    def __init__(self,cor,altura,profundidade,largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
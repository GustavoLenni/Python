# Repetições (For e While)
notas = []

for x in range(5):
    codigo_aluno = int(input("RM:"))
    nota = float(input("Nota:"))
    # no resultado ele define o indice 0 para o codigo aluno e 1 para a nota
    resultado = [codigo_aluno, nota]
    # adiciona o resultado na variavel notas 
    notas.append(resultado)

print("Quantidade de notas dos alunos", len(notas))

for n in notas:
    # pega o valor do indice do codigo aluno e retorna o a informação do usuario 
    codigo_aluno = n[0]
    #  mesma coisa para nota pegando o indice 
    nota = n[1]
    print("Rm: ", codigo_aluno, "Nota: ", nota)

notas = []

contador = 1
# o contador inicia com 1

while contador <= 5:
    # quando o contador for 6 o loop para 
    codigo_aluno = int(input("RM: "))
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    #  ele adiciona mais 1 ao contador para o loop não ser infinito
    # porque o numero 1 sempre é menor que 5 e nunca iria chegar a 6 para parar o loop
    # gerando assim um loop infinito 
    contador = contador+1
    # ou 
    #  contador += 1

print("Quantidade de notas dos alunos: ", len(notas))
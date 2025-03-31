# Funções 
print("Realize sua soma")

def funcao(valor1, valor2):
    return valor1 + valor2

contador = 1
while contador <= 5:
    
    valor1 = int(input("Valor1: "))
    valor2 = int(input("Valor2: "))
    
    resultado = funcao(valor1,valor2)
    print( valor1, "+",valor2, "=", resultado)
    print("------------")
    contador = contador+1

caixa = []

print("Fluxo de Caixa")
print("Opção 1: Adicionar Receita")
print("Opção 2: Adicionar Despesa")
print("Digite outro número para finalizar")


def transacao(opcao):
    nome = str(input("Nome: "))
    valor = float(input("Valor: "))
    caixa.append({ 
        "nome":nome,
        "valor":valor,
    })
    print("----------------")

while True:
    opcao = int(input("Digite a Opção: "))

    if opcao == 1 or opcao == 2:
        transacao(opcao)
    else:
        break


total = 0
for i in caixa:
    print("-------------")
    print("Nome: ", i['nome'], "Valor R$: ", i['valor'])
    total = total + i['valor']
    print("Saldo Atual R$: ", total)
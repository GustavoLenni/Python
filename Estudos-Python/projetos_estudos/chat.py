# Chat 
# Importando scripts 
import os

mensagens = []

nome = input("Nome: ")

while True:

    os.system('cls')

    if len(mensagens) > 0:
        for i in mensagens:
            print( i ['nome'], "-", i ['texto'])
    
    print("______________________")

    texto = input("mensagem: ")
    if texto == 'fim':
        break

    mensagens.append({
        "nome": nome,
        "texto": texto
    })
